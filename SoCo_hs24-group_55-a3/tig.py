# create a directory with two folders: 
def init(directory):
    tig_directory = Path(directory) / ".tig"
    if not tig_directory.exists():
        tig_directory.mkdir()
        (tig_directory / "staged").mkdir() # staged: for all files ready to be commited
        (tig_directory / "commits").mkdir() # commits: folders of commits