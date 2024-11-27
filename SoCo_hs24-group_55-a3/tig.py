import os
import sys
import shutil
from hashlib import sha256
import time
from datetime import datetime
from pathlib import Path
import csv
import uuid
from glob import glob

# hash is a mathematical function that given an input it gives a unique output / identifier for input and it shows where data is stored in a hash table
HASH_LEN = 16

# manifest visual =  like a table of files. first column = name of the file, second column = hash

def backup(source_dir,backup_dir): # backup from source_dir to backup_dir
    manifest = hash_all(source_dir) # manifest = a file that describes infos of other files
    timestamp = current_time() #string and is going to be used as the name of the manifest
    write_manifest(backup_dir,timestamp,manifest) #backup_dir = the directory where the manifest/backup will be written, timestamp = name of manifest, manifest = content
    copy_files(source_dir,backup_dir,manifest) # copy the files into the backup_dir and backup files will be named after hash
    return manifest

def hash_all(dir): # go through all files in the given directory dir and computes the hash and generates a table
    result = []
    for name in glob("**/*.*", root_dir=dir, recursive=True): # iterate through a directory, "**/*.*" = all the files, recursive = look through the subfolders
        full_name = Path(dir,name) # for different operating system and since glob skip a few folders path gives the full path
        with open(full_name,"rb") as f: # "rb" to read as binary files, since the file can also be non-text
            data = f.read() # read the data
            hash_code = sha256(data).hexdigest()[:HASH_LEN] # hash the data
            result.append((name,hash_code))
    return result # [ (filename.txt, sdajfhg238756), (sub/file2.txt, 348576bkfwar) ] filename & hash value


def current_time():
    return f"{time.time()}".split(".")[0]


def write_manifest(backup_dir,timestamp,manifest): # create a file with content manifest named timestamp in backup_dir
    backup_dir = Path(backup_dir) # backup_dir is no longer a string of path but a path object
    if not backup_dir.exists():
        backup_dir.mkdir() # if backup_dir doesnt exit create 
    manifest_file = Path(backup_dir, timestamp+".csv") # csv is used for manifest files
    with open(manifest_file,"w") as f: # write the content of manifest on manifest_file
        f.write("filename,hash"+"\n")
        for filename,hash_code in manifest: # manifest has a tuple (filename,hashcode)
            f.write(filename + "," + hash_code + "\n")

def copy_files(source_dir,backup_dir,manifest): # check which files need to be copied
    for (filename,hash_code) in manifest: # helo.txt, 0b8e6c43ac411146
        source_path = Path(source_dir,filename) # /Users/sback/soco/helo.txt
        backup_path = Path(backup_dir,hash_code) # /Users/sback/soco_bkp2/0b8e6c43ac411146
        if not backup_path.exists(): # changes of content --> changes hash codes
            shutil.copy(source_path,backup_path) # copy

def init(directory):
    dir_path = Path(directory)  # create path to chosen directory
    tig_dir = dir_path / ".tig"  # create path to wanted tig file

    # defensive programming
    if not dir_path.exists():
        print(f"The directory '{directory}' does not exist!")
        return

    if tig_dir.exists():
        print(f"A .tig repository already exists in '{directory}'!")
        return

    tig_dir.mkdir() # create the tig folder


def add_file(filename):
    tig_dir = Path(".tig")
    index_path = tig_dir / "index"
    filepath = Path(filename)

    if not tig_dir.exists():
        print(f"A .tig repository does not exists!")
        return

    if not filepath.exists():
        print(f"File '{filename}' does not exist!")
        return

    #calculate file hash
    with open(filepath, "rb") as file:
        file_hash = sha256(file.read()).hexdigest()

    #check if hash already in index file, if yes overwrite if changed

    if index_path.exists():
        with open(index_path, "r") as index_file:
            reader = csv.reader(index_file)
            staged_files = {row[0]: row[1] for row in reader}
    else:
        staged_files = {}

    staged_files[filename] = file_hash

    #write all staged files back to index
    with open(index_path, "w") as index_file:
        writer = csv.writer(index_file)
        for newname, newhash in staged_files.items():
            writer.writerow([newname, newhash])

    #append the filename and hash to the index
    print(f"Added '{filename}' to staging area.")

#had to write this function because we were struggling with the naming of the commit folders in commits
#and it was cleaner this way than to put it in the commit function itself

def get_next_commit_id():
    tig_dir = Path(".tig")
    last_commit_file = tig_dir / "last_commit_id"

    #check for last commit id
    if not last_commit_file.exists():
        with open(last_commit_file, "w") as f:
            f.write("0")  # Start with 0

    with open(last_commit_file, "r") as f:
        last_id = int(f.read().strip())

    next_id = last_id + 1

    #save
    with open(last_commit_file, "w") as f:
        f.write(str(next_id))

    return f"commit_{next_id:04d}"  #formats id as commit_0001, commit_0002...

def commit(commit_message):
    tig_dir = Path(".tig")
    index_path = tig_dir / "index"
    commits_dir = tig_dir / "commits"

    if not tig_dir.exists():
        print(f"A .tig repository does not exist!")
        return

    if not index_path.exists() or os.stat(index_path).st_size == 0:
        print("No staged files to commit.")
        return

    if not commits_dir.exists():
        commits_dir.mkdir()

    #generate unique commit ID and current date
    commit_id = get_next_commit_id()
    commit_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Read staged files from the index
    staged_files = []
    with open(index_path, "r") as index_file:
        reader = csv.reader(index_file)
        staged_files = list(reader)

    if not staged_files:
        print("No files in staging area to commit.")
        return

    #create new folder for this commit inside the commits folder
    commit_folder = commits_dir / commit_id
    commit_folder.mkdir()

    # Write the manifest file (filename and file hash)
    manifest_file = commit_folder / "manifest.csv"
    with open(manifest_file, "w") as manifest:
        writer = csv.writer(manifest)
        writer.writerow(["filename", "hash"])
        writer.writerows(staged_files)


    for filename, file_hash in staged_files:
        source_path = Path(filename)
        dest_path = commit_folder / filename
        shutil.copy(source_path, dest_path)

    #write info file(commit ID, date, message)
    info_file = commit_folder / "info.txt"
    with open(info_file, "w") as info:
        info.write(f"Commit ID: {commit_id}\n")
        info.write(f"Date: {commit_date}\n")
        info.write(f"Message: {commit_message}\n")

    # Clear the `index` file instead of deleting it
    with open(index_path, "w") as index_file:
        index_file.truncate()

    print(f"Committed with ID: {commit_id}")


def log(n=5):
    tig_dir = Path(".tig")
    commits_dir = tig_dir / "commits"

    if not tig_dir.exists():
        print("No tig repository!")
        return

    if not commits_dir.exists() or not any(commits_dir.iterdir()):
        print("No commits found!")
        return

    commit_folders = sorted(commits_dir.iterdir(),key=lambda folder: int(folder.name.split("_")[1]),reverse=True)
    #sort commit folders by retriving them and sorting them by their id which her is transformed into an int

    n = int(n)
    recent_commits = commit_folders[:n]

    print(f"Displaying the last {len(recent_commits)} commits:\n")

    for commit_folder in recent_commits:
        info_file = commit_folder / "info.txt"
        if not info_file.exists():
            print(f"Missing info.txt in {commit_folder.name}")
            continue

        with open(info_file, "r") as file:
            lines = file.readlines()

        commit_id = lines[0].split(":")[1].strip()  #id
        commit_date = lines[1].split(":")[1].strip()  #date
        commit_message = lines[2].split(":")[1].strip()  # message

        print(f"Commit ID: {commit_id}")
        print(f"Date: {commit_date}")
        print(f"Message: {commit_message}")
        print("-" * 30)

def get_latest_commit_files(commits_folder):
    #we tried to implement this logic directly into the status function, but it was getting too long, and it is easier to understand this way
    if not commits_folder.exists() or not any(commits_folder.iterdir()):
        return {}
    try:
        commit_folders = [folder for folder in commits_folder.iterdir() if folder.is_dir()]
        if not commit_folders:
            return {}

        latest_commit_folder = max(commit_folders, key=lambda f: os.path.getmtime(f)) #had to use GPT for this line
        manifest_file = latest_commit_folder / "manifest.csv"
    #by doing this we get the latest manifest file

        if manifest_file.exists():
            with open(manifest_file, "r") as manifest:
                reader = csv.reader(manifest)
                next(reader)  #skip header
                return {row[0]: row[1] for row in reader}
    except Exception as exception:
        print(f"Error processing commits folder: {exception}")
        return {}


def status():
    tig_dir = Path(".tig")
    index_path = tig_dir / "index"
    commits_folder = Path(".tig/commits")


    if not tig_dir.exists():
        print("Error: Not a tig repository (or .tig directory missing).")
        return

    # append all files in directory to list, except those in .tig folder (to compare later)

    files_in_working_directory = [file for file in os.listdir(".") if
                                  os.path.isfile(file) and not file.startswith(".tig")]

    staged_files = {}
    if index_path.exists():
        with open(index_path, "r") as index_file:
            reader = csv.reader(index_file)
            staged_files = {row[0]: row[1] for row in reader}


    untracked_files = []
    staged_files_status = []
    modified_staged_files = []
    modified_unstaged_files = []
    committed_files = get_latest_commit_files(commits_folder)

    for file in files_in_working_directory:
        current_hash = sha256(Path(file).read_bytes()).hexdigest()
        if file in staged_files:
            if current_hash != staged_files[file]:
                modified_staged_files.append(file)
            staged_files_status.append(file)

        elif file in committed_files:
            if current_hash != committed_files[file]:
                modified_unstaged_files.append(file)

        else:
            untracked_files.append(file)

    if staged_files_status:
        print("Staged files:")
        for file in staged_files_status:
            print(f"{file}")
    if modified_staged_files:
        print("Modified and Staged files:")
        for file in modified_staged_files:
            print(f"  {file}")
    if modified_unstaged_files:
        print("Modified and Not Staged files:")
        for file in modified_unstaged_files:
            print(f"  {file}")
    if untracked_files:
        print("Untracked files:")
        for file in untracked_files:
            print(f"{file}")
    if not staged_files_status and not modified_staged_files and not modified_unstaged_files and not untracked_files:
        print("No changes.")

#had to write this function because we were struggling with the naming of the commit folders in commits
#,and it was cleaner this way than to put it in the commit function itself

def diff(filename):
    commits_dir = Path(".tig/commits") #go to commits folder
    latest_commit = sorted(commits_dir.iterdir(), reverse=True)[0] # sort the folders in the commits and take the last commited one
    manifest_file = latest_commit / "manifest.csv" # take the manifest file in the commit folder
    with open(manifest_file, "r") as f:
        manifest = dict(line.strip().split(",") for line in f.readlines()[1:]) # read the manifest file to find the committed_file through hash 
    
    committed_file = latest_commit / manifest[filename] 

    with open(committed_file, "r") as f: 
        committed_content = f.readlines()

    with open(filename, "r") as f:
        current_content = f.readlines()

    result = difflib.unified_diff( # used automatic library function
    committed_content,
    current_content,
    lineterm="\n")
    
    print(result)


def checkout(commit_id):
    tig_dir = Path(".tig")
    commits_dir = tig_dir / "commits"
    commit_folder = commits_dir / commit_id

    #defensive coding
    if not tig_dir.exists():
        print("Not a tig repository!")
        return

    #defensive coding
    if not commit_folder.exists():
        print(f"Commit '{commit_id}' does not exist!")
        return

    manifest_file = commit_folder / "manifest.csv"
    if not manifest_file.exists():
        print(f"Manifest file for commit '{commit_id}' is missing!") #defensive coding
        return


    with open(manifest_file, "r") as manifest:
        reader = csv.reader(manifest)
        next(reader) #need to skip header of file
        file_data = {row[0]: row[1] for row in reader}


    for filename, file_hash in file_data.items():
        source_path = commit_folder / filename
        dest_path = Path(filename)

        #defensive coding
        if not source_path.exists():
            print(f"Error: File for {commit_id}'does not exist!")
            continue

        # had to use ai to figure out parent attribute of pathlib
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        
        shutil.copy(source_path, dest_path)
        

    print(f"Checkout to commit '{commit_id}' completed.")

#if __name__ == "__main__":
#    assert len(sys.argv) == 3, "Usage: backup.py source_dir dest_dir"
#    source_dir = sys.argv[1]
#    dest_dir = sys.argv[2]
#    backup(source_dir,dest_dir)


