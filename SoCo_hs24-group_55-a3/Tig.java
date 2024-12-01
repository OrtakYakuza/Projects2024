import java.io.*;
import java.nio.file.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.time.Instant;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Tig {

    public static final int HASH_LEN = 16;

 
    public record FileEntry(String filename, String hash) {}


    public static void backup(String sourceDir, String backupDir) {
        List<FileEntry> manifest = hashAll(Paths.get(sourceDir));
        String timestamp = getTimestamp();
        writeManifest(Paths.get(backupDir), timestamp, manifest);
        copyFiles(Paths.get(sourceDir), Paths.get(backupDir), manifest);
    }

    
    public String calculateHash(Path file) {
        try {
            byte[] data = Files.readAllBytes(file);  
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] hashBytes = digest.digest(data);

            
            return bytesToHex(hashBytes, HASH_LEN);

        } catch (IOException | NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
    }



    public static List<FileEntry> hashAll(Path root) {
        List<FileEntry> result = new ArrayList<>();

        try (Stream<Path> paths = Files.walk(root)) {
            List<Path> files = paths.filter(Files::isRegularFile)
                                    .collect(Collectors.toList());

            for (Path file : files) {
                String relativePath = root.relativize(file).toString();
                String hashCode = calculateHash(file);
                result.add(new FileEntry(relativePath, hashCode));
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

        return result;
    }


    public static String getTimestamp() {
        return String.valueOf(Instant.now().getEpochSecond());
    }

    public static void writeManifest(Path backupDir, String timestamp, List<FileEntry> manifest) {
        if (!Files.exists(backupDir)) {
            try {
                Files.createDirectories(backupDir);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        Path manifestFile = backupDir.resolve(timestamp + ".csv");
        try (FileWriter writer = new FileWriter(manifestFile.toFile())) {
            writer.write("filename,hash\n");
            for (FileEntry entry : manifest) {
                writer.write(entry.filename() + "," + entry.hash() + "\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void copyFiles(Path sourceDir, Path backupDir, List<FileEntry> manifest) {
        for (FileEntry entry : manifest) {
            Path sourcePath = sourceDir.resolve(entry.filename());
            Path backupPath = backupDir.resolve(entry.hash() + ".bck");
            if (!Files.exists(backupPath)) {
                try {
                    Files.copy(sourcePath, backupPath);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public static void init(String directory) throws IOException {
        Path dirPath = Paths.get(directory); // convert string into an pathobject
        Path tigDir = dirPath.resolve(".tig"); // resolve appends the tig to dirpath


        // defensive coding

        if (!Files.exists(dirPath)) {
            System.out.println("The directory '" + directory + "' does not exist!");
            return;
        }

        if (Files.exists(tigDir)) {
            System.out.println("A .tig repository already exists in '" + directory + "'!");
            return;
        }

        // creates subdirectory
        Files.createDirectory(tigDir);
    }

    public static void status() {
        Path tigDir = Paths.get(".tig");               
        Path indexPath = tigDir.resolve("index");      
        Path commitsFolder = tigDir.resolve("commits");

        if (!Files.exists(tigDir)) {                   
            System.out.println("Error: Not a tig repository (or .tig directory missing).");
            return;
        }

        try {
            
            List<Path> workingFiles = Files.list(Paths.get("."))
                    .filter(file -> Files.isRegularFile(file) && !file.getFileName().toString().startsWith(".tig"))
                    .collect(Collectors.toList());

            
            Map<String, String> stagedFiles = new HashMap<>();
            if (Files.exists(indexPath)) {
                List<String> indexEntries = Files.readAllLines(indexPath);
                for (String entry : indexEntries) {
                    String[] parts = entry.split(",");
                    if (parts.length == 2) {
                        stagedFiles.put(parts[0], parts[1]); 
                    }
                }
            }

            
            Map<String, String> committedFiles = getLatestCommitFiles(commitsFolder);

            
            List<String> untrackedFiles = new ArrayList<>();
            List<String> stagedFilesStatus = new ArrayList<>();
            List<String> modifiedStagedFiles = new ArrayList<>();
            List<String> modifiedUnstagedFiles = new ArrayList<>();
            Map<String, String> committedFilesDisplay = new HashMap<>(committedFiles);

            for (Path file : workingFiles) {
                String filename = file.getFileName().toString();
                String currentHash = calculateHash(file); 

                if (stagedFiles.containsKey(filename)) {
                    
                    if (!currentHash.equals(stagedFiles.get(filename))) {
                        modifiedStagedFiles.add(filename);
                    } else {
                        stagedFilesStatus.add(filename);
                    }
                } else if (committedFiles.containsKey(filename)) {
                   
                    if (!currentHash.equals(committedFiles.get(filename))) {
                        modifiedUnstagedFiles.add(filename);
                        committedFilesDisplay.remove(filename); 
                    }
                } else {
                    
                    untrackedFiles.add(filename);
                }
            }

           
            if (!stagedFilesStatus.isEmpty()) {
                System.out.println("Staged files:");
                stagedFilesStatus.forEach(System.out::println);
            }
            if (!modifiedStagedFiles.isEmpty()) {
                System.out.println("Modified and Staged files:");
                modifiedStagedFiles.forEach(file -> System.out.println("  " + file));
            }
            if (!modifiedUnstagedFiles.isEmpty()) {
                System.out.println("Modified and Not Staged files:");
                modifiedUnstagedFiles.forEach(file -> System.out.println("  " + file));
            }
            if (!untrackedFiles.isEmpty()) {
                System.out.println("Untracked files:");
                untrackedFiles.forEach(System.out::println);
            }
            if (!committedFilesDisplay.isEmpty()) {
                System.out.println("Committed files:");
                committedFilesDisplay.keySet().forEach(file -> System.out.println("  " + file));
            }
            if (stagedFilesStatus.isEmpty() && modifiedStagedFiles.isEmpty() &&
                modifiedUnstagedFiles.isEmpty() && untrackedFiles.isEmpty() &&
                committedFilesDisplay.isEmpty()) {
                System.out.println("No changes.");
            }
        } catch (IOException | NoSuchAlgorithmException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
