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
