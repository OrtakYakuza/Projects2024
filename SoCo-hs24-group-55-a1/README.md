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

prior to meeting up to do the last step of the assignment we all reviewed how to write tests in accordance with the lecture + book
addtionally we brainstormed ideas seperately how we would go on about solving step3 so that we can implement the proper solution together

18.10.24

we decided to first implement the test cases we wanted to do by splitting them among us three

first batch of test: 
test_beach_resort_calculate_cost_without_surfing(),test_beach_resort_calculate_cost_with_surfing(),test_adventure_trip_calculate_cost_easy(),test_adventure_trip_calculate_cost_hard(),test_luxury_cruise_calculate_cost_without_suite(),test_luxury_cruise_calculate_with_suite()
--> all of these test makes sure that when you calculate cost for a package which is correctly defined the correct output is produced, here taking into account whether the package includes its individual attribute

the second batch of tests:
test_beach_resort_describe_package_without_surfing(),test_beach_resort_describe_package_with_surfing(),test_adventure_trip_describe_package_easy(),test_adventure_trip_describe_package_hard(), test_luxury_cruise_describe_package_without_suite(), test_luxury_cruise_describe_package_with_suite()
--> all of these test makes sure that when you describe a package which is correctly defined the correct output is produced, here taking into account whether the package includes its individual attribute

the third batch of tests:
test_vacation_booking_summary_totalcost(), test_vacation_booking_summary(), test_vacation_booking_summary_AdventureTrip_totalcost(),test_vacation_booking_summary_AdventureTrip(), test_vacation_booking_summary_BeachResort_totalcost(), test_vacation_booking_summary_BeachResort(), test_vacation_booking_summary_LuxuryCruise_totalcost(),test_vacation_booking_summary_LuxuryCruise()
--> these test make sure that the vacation booking summaries are correctly produced whether that is a description or calculating the costs. the test include making a summary when no searchword is defined or when a searchword for a specific package is defined

addtionally implemented some tests for specific edge cases:

test_vacation_booking_summary_empty_totalcost()
-> this test was chosen to make sure the vacationbookingsummary class returns the correct output in every situation so even  when the list of booked holidays is empty which is what gets tested here

test_vacation_booking_summary_empty()
-> the same is done here. this test was chosen to ensure that the correct output when calling for a summary is produced when there are no bookings made 

test_adventure_trip_negative_cost
-> as there is no such thing as negative cost here we want to make sure that when a package is created with negative cost a value error is raised. here we test this by trying to make a vacation with negative cost

test_adventure_trip_calculate_cost_negative_days()
-> same goes with negative days which make no logical sense at all. the same thing as in the test before is done here to make sure a package with negative days raises an error

test_luxury_cruise_zero_days()
-> a holiday with zero days makes no sense which is what this test is for. here we make a holiday with zero days which then logically should raise a value error

test_beach_resort_invalid_surfing()
-> each of our packages has an attribute which needs to be defined when making a package (surfing,difficulty,suite) these are either a bool or for the adventurepark a string. here we make sure that when an invalid attribute is used a value error is raised. we test this here specifically with trying to describe a package

test_beach_resort_invalid_location()
-> here its the same idea but with the location for a package. we want to make sure that when eg a integer is entered instead of a string a value error is raised 

test_invalid_package()
-> we have 3 different packages from which you can choose. there are no options that should be able to work. we test that this is the case by trying to ininiate a summary with an invalid searchterm

test_invalid_searchterm()
-> we only have 3 valid classes for which the vacation booking summary classes should work if one uses a searchterm not related to our classes a value error should be raised which is what this test does. it does this by trying to make a vacation summary with an invalid searchterm

After writing the tests one of us went through all of the tests to rename and restructurize, so that theyre now organized.
for the time we researched about the time.time() function 
we didnt know how to implement the select pattern functionality so we asked chatgpt: how to implement a select pattern through terminal for running tests. Then we decided to use the sys.argv which is quite understandable

19.10.24
implemented some "defensive coding" so that errors are raised with incorrect values and tests also work accordingly

20.10.24
ran into problems with edge case tests which we solved together
tried to implement the set up/tear down function that needs to be improved

21.10.24
