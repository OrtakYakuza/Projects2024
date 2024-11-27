import sys
import os
import time
import shutil
from glob import glob
from pathlib import Path
from hashlib import sha256

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

#if __name__ == "__main__":
#    assert len(sys.argv) == 3, "Usage: backup.py source_dir dest_dir"
#    source_dir = sys.argv[1]
#    dest_dir = sys.argv[2]
#    backup(source_dir,dest_dir)

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
