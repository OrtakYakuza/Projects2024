07.10.24 - first day of working on assignment together!

started with setting up our repository and adding the required folders/files + adding members
encountered some difficulties adding a folder which led to our first ChatGPT Prompt: How to create a Folder in GitLab
looked at branches and commits/merging together so that everyone is on the same page, here we encountered difficulties with merging conflicts -> ChatGPT Prompt: Merge conflicts and how to solve them per terminal

started working on Step1 by splitting up the classes between ourselves 
Kept getting Recursion Errors on first commit on Nikolanew and had to ask ChatGPT with a copy of the code: why do I keep getting Recursion Errors
tentatively finished our classes and merged them into the main branch + created make_function that works with respectively each class

08.10.24 - second day of working on assignment

made some minor corrections to our main class
merged the make_function with the main class
added missing functions to the make_function
added some test calls to see if the code works

09.10.24

removed the prior added functions from mkae_function as we realized our other method was not ideal
made a find/call function as this is a better way 

Since we implented the find and call function, we implemented the calculate total cost and the extract total vacation summary, by creating a list (booked_holidays) and iterating over it using the call function to call calculate_cost and describe_package functions and appending them to a new list, which is summed for the cost and returned in the summary function.

we adjusted the functions to be directly connected to the the VacationBookingSummary so when a  instance is created it checks the search term which  has to be in ["_class"]["_classname"] and from there it utilizes the functions depending if the search term is None or "something".

10.10.24 - 17.10.24

prior to meeting up to do the last step of the assignemt we all reviewed how to write tests in accordance with the lecture + book
addtionally we brainstormed ideas seperately how we would go on about soliving step3 so that we can implement the proper solution together

18.10.24

we decided to first implement the test cases we wanted to do by splitting them among us