25.10.24 -- first day of assignment

as a first step,ep we copied the interpreter from Lecture4 to our main and reviewed again how it worked
while coping the interpreter we encountered a problem which we could quickly fixed

we then got to step1 which was implementing the infix operators. here we first implemented the new functions needed for the arithmetic operations  (do_plus, do_minus, do_multiply, and do_divide) and logical operations (do_and, do_or, and do_xor)

after that modified the do function so that it can handle these infix operations accordingly and the same goes for the OPS dictionary which OPS dictionary which includes both the prefixed and symbol-based versions of each operation

we also modified our example_infix.gsc file

28.10.24

made some minor corrections to our infix operator implementation, more specifically fixed the do_function so setting a variable is checked before operation, that a variable is not treated as an operation

29.10.24

now that step1 is tentatively completed we started with step2 which is implementing lexical scoping

01.11.24

before meeting up we all individually reviewed the powerpoint about stacks to refresh our memory about dynamic and lexical scoping
together we then implemented the lexical scoping in our interpreter (including nested function!)
we did this by bringing 3 particular changes to our interpreter:
1. when defining a function the do_function takes a snapshot of the current environment which is stored under func_snap_env
2. when the do_call functions is called instead of using env_stack a new environment stack is used which is made up of the func_snap_env and the local environment
3. to respect lexical scoping, the set_in_envs_stack function was updated accordingly

we wrote both a lgl file that demonstrate the lexical scoping in general and one that shows how it specifically works for nested functions

03.11.24

##logging function


08.11.24

we started implementing the second part of step3 which is the reporting file
as we have to implement a table with our results we chose to use text file format CSV which makes processing the data from trace_file.log easier 
the csv.reader reads the file row by row. each row has four fields id, timestamp, function_name, and event_type.
to turn timestamp to timestamp_ms we used the the datetime libary with which we needed some help from AI for the datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
the report_data list created by reporting_all() is then passed to display_report() which isnt finished yet


09.11.24

finished the reporting.py file to transform the trace_file-log to a table and make it look nicer and have a better overview. Additionally added colorama for optics