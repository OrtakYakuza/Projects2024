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
after we implemented all functions we merged each branch into main and tested through all the steps. There were still some problems so we updated and debugged the functions until everything works. More specifically we had to change the status and commit functio we came to this realization when our checkout function was not giving the correct output

STEP1 output of the commands:

1. mkdir repo
python3 tig.py init repo

our output: 

No specific output in terminal but the directory gets created and a tig repository is initialized.

2. cd repo
echo "Initial content" > file.txt
echo "Initial content of the other file" > other_file.txt
python3 ../tig.py status

our ouput: 

Untracked files:
file.txt
other_file.txt

3. python3 ../tig.py add file.txt
python3 ../tig.py add other_file.txt
python3 ../tig.py status

our output:

Added 'file.txt' to staging area.
Added 'other_file.txt' to staging area.
Staged files:
file.txt
other_file.txt


4. python3 ../tig.py commit "Initial commit"
python3 ../tig.py status

our output:
Committed with ID: commit_0001
Committed files:
  file.txt
  other_file.txt

5. echo "Updated content" >> file.txt
python3 ../tig.py status

our output:
Modified and Not Staged files:
  file.txt
Committed files:
  other_file.txt

6. python3 ../tig.py diff file.txt

our output:
+++ 
@@ -1 +1,2 @@
 Initial content

+Updated content

7. python3 ../tig.py add file.txt
python3 ../tig.py commit "Updated content in file.txt"

our output:

Added 'file.txt' to staging area.
Committed with ID: commit_0002

8. python3 ../tig.py log
python3 ../tig.py checkout commit_0001

our output:

Displaying the last 2 commits:

Commit ID: commit_0002
Date: 2024-12-01 17
Message: Updated content in file.txt
------------------------------
Commit ID: commit_0001
Date: 2024-12-01 17
Message: Initial commit
------------------------------
Checkout to commit 'commit_0001' completed.

9. python3 ../tig.py status

our output:

Modified and Not Staged files:
  file.txt
Committed files:
  other_file.txt


29.11.24

As we have officially finished Step1 we move on to Step2!
reviewed lecture with java file archiver
implemented file archiver in our tig.py within our tig class as java is object oriented
with this we offical start with step2!

30.11.24 - 03.12.24

as a first step we devided the function among us and rewrote them in java on seperate branches here we used chatgpt as help to figure out certain functionalities
we then merged them all together into our main 

when we first ran the code then we quickly came to the realization that our code was not working and was showing errors and faults which made it impossible. The main issue was that the file was inconsistent and incomplete handling of file paths, variables (like directory and TIG_DIR), and static methods.

we continued by debugging our faulty file and to make it work like it should for this we first removed the redunant part of the file archiver which were unecessary to our code 

the second part was fixing the faults which were leading our code not to run which were the ones metioned above

after the code was now able to run we tried running the commands we here quickly realized that our status function was not giving the correct output. here we had to debug for quite a while to make status give the correct output and also had to modify commit as they status for the commited files was not showing up correct.

in general we had difficulty with writing java code because of its static nature, it is very different from pythons dynamic one 

STEP2 output of the commands:

1. mkdir repo_java
java Tig.java init repo_java

our output:
Initialized empty Tig 

2. cd repo
echo "Initial content" > file.txt
echo "Initial content of the other file" > other_file.txt
java ../Tig status

our output:
Committed files:
(none)

Staged files:
(none)

Modified files:
(none)

Untracked files:
file.txt
other_file.txt

3. java ../Tig add file.txt
java ../Tig add other_file.txt
java ../Tig status

our output:
Added 'file.txt' to staging area.
Added 'other_file.txt' to staging area.
Committed files:
(none)

Staged files:
file.txt
other_file.txt

Modified files:
(none)

Untracked files:
(none)

4.  java ../Tig commit "Initial commit"
java ../Tig status

our output:
"Initial commit"
Committed with ID: commit_0001
Committed files:
file.txt
other_file.txt

Staged files:
(none)

Modified files:
(none)

Untracked files:
(none)

5. echo "Updated content" >> file.txt
java ../Tig status

our output:
Committed files:
other_file.txt

Staged files:
(none)

Modified files:
file.txt

Untracked files:
(none)

6. java ../Tig diff file.txt

our output:
Differences for file: file.txt
---------------------------
  Initial content
+ Updated content

7. java ../Tig add file.txt
java ../Tig commit "Updated content in file.txt"

our output:
"Updated content in file.txt"
Committed with ID: commit_0002


8. java ../Tig log
java ../Tig checkout commit_0001

our output:
Commit ID: commit_0002
Message: Updated content in file.txt
Date: 2024-12-02T16:24:59.557345Z
-----------------------------
Commit ID: commit_0001
Message: Initial commit
Date: 2024-12-02T16:23:46.867794Z
-----------------------------

9. java ../Tig status

our output:
Committed files:
other_file.txt

Staged files:
(none)

Modified files:
file.txt

Untracked files:
(none)


