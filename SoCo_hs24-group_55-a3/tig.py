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