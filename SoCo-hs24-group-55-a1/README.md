07.10.24 - First day of working on the assignment together!  
We started by setting up our repository, adding the required folders/files, and adding members. We encountered some difficulties adding a folder, which led to our first ChatGPT prompt: "How to create a folder in GitLab."  
We looked at branches, commits, and merging to ensure everyone was on the same page. Here we encountered difficulties with merging conflicts, leading to the next ChatGPT prompt: "Merge conflicts and how to solve them via terminal."  
We created our first branch, besides the main one, called "parent class," where we defined our parent class called `VacationPackage`.  
We started working on Step 1 by splitting up the classes among ourselves and creating separate branches for them (AdventureTrip, LuxuryCruise, BeachResort).  
We kept getting recursion errors on the first commit in the "Nikolanew" branch and had to ask ChatGPT with a copy of the code: "Why do I keep getting recursion errors?"  
We tentatively finished our classes and merged them into the main branch, where we encountered some merge conflicts that we solved. Additionally, we created `make_function` on a new branch that works with each class.

---

08.10.24  
We made some minor corrections to our main class within our subclasses.  
We merged the `make_function` branch with the main class, which caused a merge issue that was fixed.  
We added missing functions to the `make_function` and added some test calls to check if the code works.

---

09.10.24  
We removed the prior added functions from `make_function` as we realized our initial method was not ideal, and that a `find/call` function would be better.  
Therefore, we created a new branch for the `find/call` function, which was then merged with the main branch.  
Since we implemented the `find/call` function, we finished Step 1 and moved forward to Step 2 with the `VacationBookingSummary` class.  
We implemented the "calculate total cost" and "extract total vacation summary" functions by creating a list (`booked_holidays`) and iterating over it using the `call` function to call `calculate_cost` and `describe_package` functions. These were then appended to a new list, summed for the cost, and returned in the summary function.  
We adjusted the functions to be directly connected to the `VacationBookingSummary` so that when an instance is created, it checks the search term, which has to be in `["_class"]["_classname"]`. From there, it utilizes the functions depending on whether the search term is `None` or "something."

---

10.10.24 - 17.10.24  
Before meeting up to do the last step of the assignment, we all reviewed how to write tests according to the lecture and book.  
Additionally, we brainstormed ideas separately about how we would solve Step 3 so that we could implement the proper solution together.

---

18.10.24  
We decided to first implement the test cases by splitting them among the three of us and creating different branches.  
The first batch of tests:  
- `test_beach_resort_calculate_cost_without_surfing()`
- `test_beach_resort_calculate_cost_with_surfing()`
- `test_adventure_trip_calculate_cost_easy()`
- `test_adventure_trip_calculate_cost_hard()`
- `test_luxury_cruise_calculate_cost_without_suite()`
- `test_luxury_cruise_calculate_with_suite()`  

These tests ensure that when you calculate the cost for a correctly defined package, the correct output is produced, taking into account whether the package includes its individual attribute.  

The second batch of tests:  
- `test_beach_resort_describe_package_without_surfing()`
- `test_beach_resort_describe_package_with_surfing()`
- `test_adventure_trip_describe_package_easy()`
- `test_adventure_trip_describe_package_hard()`
- `test_luxury_cruise_describe_package_without_suite()`
- `test_luxury_cruise_describe_package_with_suite()`  

These tests ensure that when you describe a correctly defined package, the correct output is produced, taking into account whether the package includes its individual attribute.  

The third batch of tests:  
- `test_vacation_booking_summary_totalcost()`
- `test_vacation_booking_summary()`
- `test_vacation_booking_summary_AdventureTrip_totalcost()`
- `test_vacation_booking_summary_AdventureTrip()`
- `test_vacation_booking_summary_BeachResort_totalcost()`
- `test_vacation_booking_summary_BeachResort()`
- `test_vacation_booking_summary_LuxuryCruise_totalcost()`
- `test_vacation_booking_summary_LuxuryCruise()`  

These tests ensure that the vacation booking summaries are correctly produced, whether they describe a package or calculate the costs. The tests include making a summary when no search term is defined or when a search term for a specific package is defined.  

We additionally implemented some tests for specific edge cases on a new branch:  
- `test_adventure_trip_negative_cost()`
    - Since there’s no such thing as a negative cost, we want to ensure that when a package is created with a negative cost, a `ValueError` is raised. This is tested by trying to make a vacation with a negative cost.  
- `test_adventure_trip_negative_days()`
    - Similarly, negative days make no logical sense. We ensure that a package with negative days raises an error, as in the previous test.  
- `test_luxury_cruise_zero_days()`
    - A holiday with zero days makes no sense, which is what this test ensures. A holiday with zero days should raise a `ValueError`.  
- `test_beach_resort_invalid_surfing()`
    - Each of our packages has an attribute that needs to be defined when making a package (surfing, difficulty, suite). These are either a `bool` or, for the AdventurePark, a `string`. Here, we make sure that when an invalid attribute is used, a `ValueError` is raised. This is specifically tested with a Beach Resort package.  
- `test_beach_resort_invalid_location()`
    - Similarly, the location for a package must be a valid string. We make sure that when an invalid input (e.g., an integer) is entered, a `ValueError` is raised.  
- `test_invalid_package()`
    - There are three packages from which you can choose. No other options should work. We test this by trying to initiate a summary with an invalid search term.  
- `test_invalid_searchterm()`
    - We only have three valid classes for which the vacation booking summary classes should work. If an invalid search term unrelated to our classes is used, a `ValueError` should be raised. This is tested by trying to create a vacation summary with an invalid search term.  

After writing and merging the tests, one of us went through them to rename and restructure them, ensuring they were organized.

---

For the time function, we researched the `time.time()` function, which we then implemented.  
We didn’t know how to implement the select pattern functionality, so we researched and asked ChatGPT: "How to implement a select pattern through terminal for running tests." With the given information, we decided to use `sys.argv` to implement our solution, which is quite understandable.  
Additionally, we used ChatGPT to get a better understanding of the Colorama documentation with the prompt: "How do I modify the terminal output using Colorama? Give me an overview of the syntax."

---

19.10.24  
We implemented some defensive coding in our `vacation_booking.py` file so that errors are raised with incorrect values, and tests also work accordingly.

---

20.10.24  
We ran into problems with our edge case testing, which we solved together, and then merged into the main branch after resolving merge issues.  
We tried to implement the setup/teardown function that needed to be improved and realized that our tests for the vacation booking summary were not functioning properly.

---

21.10.24  
We fixed the tests for the vacation summary as they weren’t working correctly before, and fixed our setup/teardown function.  
We also changed `({time.time() - start_time:.2f})` to `({time.time() - start_time:.5f})` so one can better see the runtime.  
Now, our test function works as needed, meaning we have gone through all the steps!  
We finalized our assignment with a 3-hour call, where we went through the code and tests together to ensure everything worked as expected.

--- 


