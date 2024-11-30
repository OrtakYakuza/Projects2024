18.11.24

we reviewed the file archiver discussed in class together and reviewed the functionlities we have to implement for our tig implementation

22.11.24

copied the file archiver to our main w our comments
started working on step and created some branches w our implementation of our code more specifically:

we implemented the init function which initializes a .tig repository by creating a .tig folder in the specified directory
the add file fucntion which stages a file for tracking by calculating its hash and recording it in the .tig/index file
the commit function which commits all staged files by moving them to the committed state and records a unique commit ID, commit date, and commit message here we used an extra function called get_next_commit_id() which made the naming of our folders easier

26.11.24

continued working on our code together

decided to update our status functions so that it works correctly:
in order to implement modified and commited files in status function we "had" to create a new function (get_latest_commit_files) to make it easier to understand which we then used to implement the logic in the status function, which now differentiates between Modified and Staged files and Modified and Not Staged files

implement the log - N functionality which retrieves the details of the most recent commits, with a default limit of 5 commits. It does this by retrieving and sorting commit information from the .tig/commits directory 

started working on diff and checkout as well 
for the diff function we used the library method which we had to looked up on the internet and familiarize with the usage 
check out restores the repository's state to a specified commit by retrieving the commit's manifest, cleaning the current working directory + copying the files associated with the commit from the .tig/commits directory

27.11.24
after we implemented all functions we merged each branch into main and tested through all the steps. There were still some problems so we updated and debugged the functions until everything works.