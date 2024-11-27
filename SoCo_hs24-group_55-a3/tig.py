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