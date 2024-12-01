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

    public static void commit(String commitMessage) {
        Path tigDir = Paths.get(".tig");                 
        Path indexPath = tigDir.resolve("index");        
        Path commitsDir = tigDir.resolve("commits");     

        try {
            if (!Files.exists(tigDir)) {                 
                System.out.println("A .tig repository does not exist!");
                return;
            }

            if (!Files.exists(commitsDir)) {             
                Files.createDirectory(commitsDir);
            }

            Map<String, String> committedFiles = getLatestCommitFiles(commitsDir);

            
            Map<String, String> stagedFiles = new HashMap<>();

            if (Files.exists(indexPath)) {
                List<String> indexEntries = Files.readAllLines(indexPath);
                for (String entry : indexEntries) {
                    String[] parts = entry.split(",");
                    stagedFiles.put(parts[0], parts[1]);
                }
            }

            if (stagedFiles.isEmpty() && committedFiles.isEmpty()) { 
                System.out.println("No staged files to commit.");
                return;
            }

            
            String commitId = getNextCommitId(tigDir.resolve("last_commit_id"));
            String commitDate = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date());

            
            Path commitFolder = commitsDir.resolve(commitId);
            Files.createDirectory(commitFolder);

            
            Map<String, String> finalCommitFiles = new HashMap<>(committedFiles);
            finalCommitFiles.putAll(stagedFiles);

            
            Path manifestFile = commitFolder.resolve("manifest.csv");
            try (BufferedWriter writer = Files.newBufferedWriter(manifestFile)) {
                writer.write("filename,hash\n");
                for (Map.Entry<String, String> entry : finalCommitFiles.entrySet()) {
                    writer.write(entry.getKey() + "," + entry.getValue() + "\n");
                }
            }

            
            for (String filename : finalCommitFiles.keySet()) {
                Path sourcePath = Paths.get(filename);
                Path destPath = commitFolder.resolve(filename);
                if (!Files.exists(sourcePath)) continue; 

                Files.createDirectories(destPath.getParent());

                
                Files.copy(sourcePath, destPath, StandardCopyOption.REPLACE_EXISTING);
            }

            Path infoFile = commitFolder.resolve("info.txt");
            try (BufferedWriter writer = Files.newBufferedWriter(infoFile)) {
                writer.write("Commit ID: " + commitId + "\n");
                writer.write("Date: " + commitDate + "\n");
                writer.write("Message: " + commitMessage + "\n");
            }

            Files.write(indexPath, Collections.emptyList());

            System.out.println("Committed with ID: " + commitId);

        } catch (IOException e) {
            System.out.println("Error during commit: " + e.getMessage());
        }
    }

}
