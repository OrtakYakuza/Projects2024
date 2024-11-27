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


HASH_LEN = 16

def hash_all(root):
    result = []
    for name in glob("**/*.*", root_dir=root, recursive=True):
        full_name = Path(root, name)
        with open(full_name, "rb") as reader:
            data = reader.read()
            hash_code = sha256(data).hexdigest()[:HASH_LEN]
            result.append((name, hash_code))
    return result


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

    tig_dir.mkdir()
    # create the tig folder


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

    # Calculate file hash
    with open(filepath, "rb") as file:
        file_hash = sha256(file.read()).hexdigest()

    # check if hash already in index file, if yes overwrite if changed

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

    # Append the filename and hash to the index
    print(f"Added '{filename}' to staging area.")

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

