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

09.11.24

finished the reporting.py file to transform the trace_file-log to a table and make it look nicer and have a better overview. Additionally added colorama for optics