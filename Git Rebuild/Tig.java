import java.io.*;
import java.nio.file.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.time.Instant;
import java.util.*;
import java.util.function.Consumer;
import java.util.stream.Collectors;

public class Tig {

    public static final int HASH_LEN = 16; // defines the length of the hash to be used when representing file content hashes.
    public static final String TIG_DIR = ".tig"; // specifies the name of the directory that stores

    public static record FileEntry(String filename, String hash) {} // this is to to encapsulate information about a file
    
    private static Set<String> readTigIgnore() {
    Path tigIgnorePath = Paths.get(TIG_DIR, ".tigignore");
    Set<String> ignoredFiles = new HashSet<>();
    if (Files.exists(tigIgnorePath)) {
        try {
            List<String> lines = Files.readAllLines(tigIgnorePath);
            ignoredFiles.addAll(lines.stream().map(String::trim).filter(line -> !line.isEmpty()).collect(Collectors.toSet()));
        } catch (IOException e) {
            System.out.println("Error reading .tigignore: " + e.getMessage());
        }
    }
    return ignoredFiles;
    }

    public static String calculateHash(Path file) {
        try {
            byte[] data = Files.readAllBytes(file); // reads the entire content of the file into a byte array
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] hashBytes = digest.digest(data);
            return bytesToHex(hashBytes, HASH_LEN);
        } catch (IOException | NoSuchAlgorithmException e) { // handles exceptions that may occur while reading the file
            e.printStackTrace();
            return null;
        }
    }

    private static String bytesToHex(byte[] bytes, int length) {
        StringBuilder sb = new StringBuilder(); // used to construct hexidecimal string
        for (int i = 0; i < Math.min(bytes.length, length); i++) {
            sb.append(String.format("%02x", bytes[i]));
        }
        return sb.toString();
    }



    public static void init(String[] args) {
    // checks if the correct number of arguments is given 
    if (args.length != 1) {
        System.out.println("Usage: init <directory>");
        return; // exit 
    }

    // directory name from the arguments
    String directory = args[0];
    // create a Path object 
    Path dirPath = Paths.get(directory);
    // create a Path object for the '.tig' directory 
    Path tigDir = dirPath.resolve(TIG_DIR);

    try {
        // defensive coding
        if (!Files.exists(dirPath)) {
            System.out.println("The directory '" + directory + "' does not exist!");
            return; 
        }

        // defensive coding
        if (Files.exists(tigDir)) {
            System.out.println("A .tig repository already exists in '" + directory + "'!");
            return; 
        }

        // creats the '.tig' directory 
        Files.createDirectory(tigDir);
        System.out.println("Initialized empty Tig repository in " + tigDir);
    } catch (IOException e) {
        // error message
        System.out.println("Error initializing repository: " + e.getMessage());
    }
}



    public static void addFile(String[] args) {
    if (args.length != 1) {
        System.out.println("Usage: add <filename>");
        return; 
    }

    // filename from the arguments
    String filename = args[0];
    // path to tig directory
    Path tigPath = Paths.get(TIG_DIR);
    // path to index file 
    Path indexPath = tigPath.resolve("index");
    Path filepath = Paths.get(filename);

    Set<String> ignoredFiles = readTigIgnore();
    if (ignoredFiles.contains(filename)) {
    System.out.println("File '" + filename + "' is ignored as per .tigignore.");
    return;
    }



    // defensive coding
    try {
        if (!Files.exists(tigPath)) {
            System.out.println("A .tig repository does not exist!");
            return; 
        }

        
        if (!Files.exists(filepath)) {
            System.out.println("File '" + filename + "' does not exist!");
            return; 
        }

        // hash of the file
        String fileHash = calculateHash(filepath);

        // list to store index 
        List<String> indexEntries = new ArrayList<>();
        if (Files.exists(indexPath)) {
            indexEntries = Files.readAllLines(indexPath);
        }

        // check index
        boolean updated = false;
        for (int i = 0; i < indexEntries.size(); i++) {
            String[] parts = indexEntries.get(i).split(",");
            if (parts[0].equals(filename)) {
                // update hash
                indexEntries.set(i, filename + "," + fileHash);
                updated = true;
                break;
            }
        }

        // new entry
        if (!updated) {
            indexEntries.add(filename + "," + fileHash);
        }

        // update index entries 
        Files.write(indexPath, indexEntries);
        System.out.println("Added '" + filename + "' to staging area.");
    } catch (IOException e) {
        System.out.println("Error adding file: " + e.getMessage());
        
    }
}



    public static void commit(String[] args) {
    if (args.length != 1) {
        System.out.println("Usage: commit <message>");
        return; 
    }

    
    String commitMessage = args[0];
    Path tigDir = Paths.get(TIG_DIR);
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

        // get the list of staged files 
        List<String> stagedFiles = Files.exists(indexPath) ? Files.readAllLines(indexPath) : new ArrayList<>();
        if (stagedFiles.isEmpty()) {
            System.out.println("No staged files to commit.");
            return;
        }

        // a map is used to track files 
        Map<String, String> previousCommittedFiles = new HashMap<>();
        // find the latest commit folder 
        Optional<Path> latestCommit = Files.list(commitsDir)
                .filter(Files::isDirectory)
                .max(Comparator.comparing(Path::getFileName));

        if (latestCommit.isPresent()) {
            // if previous commit .read manifest file
            Path manifestPath = latestCommit.get().resolve("manifest.csv");
            if (Files.exists(manifestPath)) {
                List<String> lines = Files.readAllLines(manifestPath);
                // store info
                for (String line : lines.subList(1, lines.size())) { // Skip header
                    String[] parts = line.split(",");
                    previousCommittedFiles.put(parts[0], parts[1]);
                }
            }
        }

        Set<String> ignoredFiles = readTigIgnore();

        // add files from previous commit 
        for (Map.Entry<String, String> entry : previousCommittedFiles.entrySet()) {
            String filename = entry.getKey();
            String hash = entry.getValue();
            boolean alreadyStaged = stagedFiles.stream()
                .anyMatch(s -> s.startsWith(filename + ",")) || ignoredFiles.contains(filename);
            if (!alreadyStaged) {
                stagedFiles.add(filename + "," + hash);
            }
        }

        //  new commit ID 
        int commitId = (int) Files.list(commitsDir).count() + 1;
        String commitFolderName = String.format("commit_%04d", commitId);
        // path commit folder
        Path commitFolder = commitsDir.resolve(commitFolderName);
        Files.createDirectory(commitFolder);

        // write manifest file for commit
        Path manifestFile = commitFolder.resolve("manifest.csv");
        try (BufferedWriter writer = Files.newBufferedWriter(manifestFile)) {
            writer.write("filename,hash\n"); // header
            for (String entry : stagedFiles) {
                writer.write(entry + "\n"); // information
            }
        }

        // copy file into folder
        for (String entry : stagedFiles) {
            String[] parts = entry.split(",");
            Path sourcePath = Paths.get(parts[0]); 
            Path destPath = commitFolder.resolve(parts[0]); 
            Files.createDirectories(destPath.getParent()); 
            Files.copy(sourcePath, destPath, StandardCopyOption.REPLACE_EXISTING); 
        }

        // write info.txt file
        Path infoFile = commitFolder.resolve("info.txt");
        try (BufferedWriter writer = Files.newBufferedWriter(infoFile)) {
            writer.write("Commit ID: " + commitFolderName + "\n");
            writer.write("Message: " + commitMessage + "\n");
            writer.write("Date: " + Instant.now().toString() + "\n");
        }

        // clear the staging area  w index
        Files.delete(indexPath);
        System.out.println("Committed with ID: " + commitFolderName);
    } catch (IOException e) {
        System.out.println("Error committing changes: " + e.getMessage());
    }
}


   public static void log(String[] args) {
    
    Path tigDir = Paths.get(TIG_DIR);
    Path commitsDir = tigDir.resolve("commits");

    try {
        
        if (!Files.exists(tigDir)) {
            System.out.println("No Tig repository!");
            return; 
        }


        if (!Files.exists(commitsDir)) {
            System.out.println("No commits found!");
            return; 
        }

        // list all directories of the commits
        List<Path> commitFolders = Files.list(commitsDir)
                .filter(Files::isDirectory) // filter directories
                .sorted(Comparator.comparing((Path path) -> path.getFileName().toString()).reversed()) 
                // descending order 
                .collect(Collectors.toList()); 

        
        for (Path commitFolder : commitFolders) {
            Path infoFile = commitFolder.resolve("info.txt");
            if (Files.exists(infoFile)) {
                Files.lines(infoFile).forEach(System.out::println);
                // separator line
                System.out.println("-----------------------------");
            }
        }
    } catch (IOException e) {
        System.out.println("Error reading logs: " + e.getMessage());
        
    }
}

    public static void status(String[] args) {
    Path tigDir = Paths.get(TIG_DIR);
    Path indexPath = tigDir.resolve("index");
    Path commitsDir = Paths.get(tigDir.toString(), "commits");

    if (!Files.exists(tigDir)) {
        System.out.println("Not a Tig repository.");
        return; 
    }

    try {
        //latest commit folder
        Optional<Path> latestCommit = Files.exists(commitsDir) ?
            Files.list(commitsDir) 
                .filter(Files::isDirectory) 
                .max(Comparator.comparing(Path::getFileName)) : 
            Optional.empty(); 

        //map to store committed files and their hashes
        Map<String, String> committedFiles = new HashMap<>();
        if (latestCommit.isPresent()) {
            Path manifestPath = latestCommit.get().resolve("manifest.csv");
            if (Files.exists(manifestPath)) {
                List<String> lines = Files.readAllLines(manifestPath);
                for (String line : lines.subList(1, lines.size())) { 
                    String[] parts = line.split(",");
                    committedFiles.put(parts[0], parts[1]); 
                }
            }
        }

        //read .tigignore file
        Set<String> ignoredFiles = readTigIgnore();

        //list all files in working directory
        List<Path> workingFiles = Files.list(Paths.get("."))
            .filter(file -> !file.getFileName().toString().startsWith(".")) 
            .filter(file -> !ignoredFiles.contains(file.getFileName().toString()))
            .collect(Collectors.toList());

        //read index file for staged files
        List<String> indexEntries = Files.exists(indexPath) ? Files.readAllLines(indexPath) : new ArrayList<>();
        Set<String> stagedFiles = indexEntries.stream()
            .map(entry -> entry.split(",")[0])
            .collect(Collectors.toSet());

        // Lists to track untracked, modified, and committed files
        List<String> untrackedFiles = new ArrayList<>();
        List<String> modifiedFiles = new ArrayList<>();
        List<String> committedFileNames = new ArrayList<>(committedFiles.keySet());

        // Compare working directory files
        for (Path workingFile : workingFiles) {
            String fileName = workingFile.getFileName().toString(); 
            String currentHash = calculateHash(workingFile); 

            if (stagedFiles.contains(fileName)) {
                // If staged, remove from the committed files list
                committedFileNames.remove(fileName);
            } else if (committedFiles.containsKey(fileName)) {
                // If committed, check if it has been modified
                if (!committedFiles.get(fileName).equals(currentHash)) {
                    modifiedFiles.add(fileName); 
                    committedFileNames.remove(fileName); 
                }
            } else {
                // Add it to untracked files if none of the above
                untrackedFiles.add(fileName);
            }
        }

        //print committed files
        System.out.println("Committed files:");
        if (committedFileNames.isEmpty()) {
            System.out.println("(none)");
        } else {
            committedFileNames.forEach(System.out::println);
        }

        //print staged files
        System.out.println("\nStaged files:");
        if (stagedFiles.isEmpty()) {
            System.out.println("(none)");
        } else {
            stagedFiles.forEach(System.out::println);
        }

        //print modified files
        System.out.println("\nModified files:");
        if (modifiedFiles.isEmpty()) {
            System.out.println("(none)");
        } else {
            modifiedFiles.forEach(System.out::println);
        }

        //print untracked files
        System.out.println("\nUntracked files:");
        if (untrackedFiles.isEmpty()) {
            System.out.println("(none)");
        } else {
            untrackedFiles.forEach(System.out::println);
        }

    } catch (IOException e) {
        System.out.println("Error checking status: " + e.getMessage());
    }
}


    public static void diff(String[] args) {
    if (args.length != 1) {
        System.out.println("Usage: diff <filename>");
        return; 
    }

    
    String filename = args[0];
    Path tigDir = Paths.get(TIG_DIR);
    Path commitsDir = tigDir.resolve("commits");
    Set<String> ignoredFiles = readTigIgnore();
    if (ignoredFiles.contains(filename)) {
        System.out.println("File '" + filename + "' is ignored as per .tigignore.");
        return;
    }


   
    if (!Files.exists(tigDir)) {
        System.out.println("Not a Tig repository.");
        return; 
    }

    try {
        // latest commit folder
        Optional<Path> latestCommit = Files.exists(commitsDir) ?
            Files.list(commitsDir) // list all files 
                .filter(Files::isDirectory) // filter 
                .max(Comparator.comparing(Path::getFileName)) : 
            Optional.empty(); // empty optional

        if (latestCommit.isEmpty()) {
            System.out.println("No commits found for comparison.");
            return; 
        }

        // manifest file of latest commit
        Path manifestPath = latestCommit.get().resolve("manifest.csv");
        if (!Files.exists(manifestPath)) {
            System.out.println("Manifest file is missing in the latest commit.");
            return; 
        }

        
        Map<String, String> committedFiles = new HashMap<>();
        List<String> manifestLines = Files.readAllLines(manifestPath); 
        for (String line : manifestLines.subList(1, manifestLines.size())) { 
            String[] parts = line.split(","); 
            committedFiles.put(parts[0], parts[1]); 
        }

    
        if (!committedFiles.containsKey(filename)) {
            System.out.println("File '" + filename + "' was not committed in the latest commit.");
            return; 
        }


        Path committedFilePath = latestCommit.get().resolve(filename);
        if (!Files.exists(committedFilePath)) {
            System.out.println("Committed file '" + filename + "' is missing in the repository.");
            return; 
        }
        
        List<String> committedContent = Files.readAllLines(committedFilePath);

        // current version 
        Path workingFilePath = Paths.get(filename);
        if (!Files.exists(workingFilePath)) {
            System.out.println("Working file '" + filename + "' does not exist.");
            return; 
        }
        
        List<String> workingContent = Files.readAllLines(workingFilePath);

        
        System.out.println("Differences for file: " + filename);
        System.out.println("---------------------------");

        
        int maxLines = Math.max(committedContent.size(), workingContent.size());
        for (int i = 0; i < maxLines; i++) {
            String committedLine = i < committedContent.size() ? committedContent.get(i) : null;
            String workingLine = i < workingContent.size() ? workingContent.get(i) : null;

            
            if (Objects.equals(committedLine, workingLine)) {
                System.out.println("  " + (committedLine != null ? committedLine : ""));
            } else {
                if (committedLine != null) {
                    System.out.println("- " + committedLine); 
                }
                if (workingLine != null) {
                    System.out.println("+ " + workingLine); 
                }
            }
        }
    } catch (IOException e) {
        System.out.println("Error performing diff: " + e.getMessage());
        
    }
}

    public static void checkout(String[] args) {
    if (args.length != 1) {
        System.out.println("Usage: checkout <commit_id>");
        return; 
    }

    // extract info
    String commitId = args[0];
    Path tigDir = Paths.get(TIG_DIR);
    Path commitsDir = tigDir.resolve("commits");
    Path commitFolder = commitsDir.resolve(commitId);

    
    if (!Files.exists(tigDir)) {
        System.out.println("Not a Tig repository!");
        return; 
    }

    
    // defensive coding
    if (!Files.exists(commitFolder)) {
        System.out.println("Commit '" + commitId + "' does not exist!");
        return; 
    }

    // defensive coding
    Path manifestFile = commitFolder.resolve("manifest.csv");
    if (!Files.exists(manifestFile)) {
        System.out.println("Manifest file for commit '" + commitId + "' is missing!");
        return; 
    }

    try {
        // readmanifest file for info 
        Map<String, String> committedFiles = new HashMap<>();
        List<String> lines = Files.readAllLines(manifestFile);
        for (String line : lines.subList(1, lines.size())) { 
            String[] parts = line.split(","); 
            committedFiles.put(parts[0], parts[1]); // store in map
        }

        // remove all files 
        Files.list(Paths.get("."))
            .filter(path -> !path.getFileName().toString().startsWith(".tig")) // Exclude .tig directory
            .forEach(path -> {
                try {
                    if (Files.isDirectory(path)) {
                        Files.walk(path)
                            .sorted(Comparator.reverseOrder()) 
                            .forEach(p -> {
                                try {
                                    Files.delete(p); 
                                } catch (IOException e) {
                                    System.out.println("Error deleting " + p + ": " + e.getMessage());
                                }
                            });
                    } else {
                        Files.delete(path);
                    }
                } catch (IOException e) {
                    System.out.println("Error cleaning up working directory: " + e.getMessage());
                }
            });

        Set<String> ignoredFiles = readTigIgnore();

        // restore committed files
        for (Map.Entry<String, String> entry : committedFiles.entrySet()) {
            if (ignoredFiles.contains(entry.getKey())) continue;
            Path sourcePath = commitFolder.resolve(entry.getKey());
            Path destPath = Paths.get(entry.getKey());
        

        
            if (destPath.getParent() != null) {
                Files.createDirectories(destPath.getParent());
            }

            // copy files
            Files.copy(sourcePath, destPath, StandardCopyOption.REPLACE_EXISTING);
        }

        
        System.out.println("Checked out to commit '" + commitId + "'.");
    } catch (IOException e) {
        System.out.println("Error during checkout: " + e.getMessage());

    }
}


    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage: java Tig <command> [arguments]");
            return;
        }

        String command = args[0];
        String[] commandArgs = Arrays.copyOfRange(args, 1, args.length);

        Map<String, Consumer<String[]>> commands = new HashMap<>();
        commands.put("init", Tig::init);
        commands.put("add", Tig::addFile);
        commands.put("commit", Tig::commit);
        commands.put("log", Tig::log);
        commands.put("status", Tig::status);
        commands.put("checkout", Tig::checkout);
        commands.put("diff", Tig::diff);

        if (commands.containsKey(command)) {
            commands.get(command).accept(commandArgs);
        } else {
            System.out.println("Unknown command: " + command);
        }
    }
}

    