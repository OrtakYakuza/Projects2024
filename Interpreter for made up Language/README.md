
# Project Assignment Log

### 25.10.24  
**First Day of Assignment**  
- Copied the interpreter from *Lecture 4* into our main file and reviewed its functionality.
- Encountered a minor issue during the copy process, which we quickly resolved.
- Started **Step 1**: Implementing infix operators.  
  - Created new functions for arithmetic operations (`do_plus`, `do_minus`, `do_multiply`, `do_divide`) and logical operations (`do_and`, `do_or`, `do_xor`).
  - Modified the `do` function to handle these infix operations and updated the `OPS` dictionary to support both prefix and symbol-based versions of each operation.
  - Made updates to `example_infix.gsc` for testing.

### 28.10.24  
- Minor corrections to the infix operator implementation:
  - Adjusted the `do_function` to check for variable settings before operation processing, ensuring that variables aren’t mistaken for operations.

### 29.10.24  
**Started Step 2: Implementing Lexical Scoping**  
- Began working on lexical scoping in the interpreter.

### 01.11.24  
- Prior to group work, we individually reviewed the PowerPoint on stacks to refresh concepts of dynamic and lexical scoping.
- Implemented lexical scoping in our interpreter, including nested functions, by making these changes:
  - `do_function` now takes a snapshot of the current environment, saved as `func_snap_env`.
  - `do_call` utilizes a new environment stack, combining `func_snap_env` with the local environment.
  - Updated `set_in_envs_stack` to respect lexical scoping.
- Created two `.lgl` files: one demonstrating general lexical scoping and another showing how it works in nested functions.

### 03.11.24  
**Started Working on the Logging Feature**  
- Consulted the course book and created a logging function with a unique ID generator and decorator.
- Integrated these features into the main function to access logs with `--trace`.

### 08.11.24  
**Step 3, Part 2: Reporting Feature**  
- Began implementing the reporting functionality with CSV output format to process data from `trace_file.log` efficiently.
  - Used `csv.reader` to read each row containing `id`, `timestamp`, `function_name`, and `event_type`.
  - For accurate time representation, converted `timestamp` to `timestamp_ms` using `datetime.strptime()`.
- Created a `report_data` list in `reporting_all()` and passed it to `display_report()` (still in progress).

### 09.11.24  
- Completed `reporting.py` to transform `trace_file.log` into a structured table for improved readability, adding `colorama` for visual enhancements.
- Merged all branches into `main` and resolved conflicts.

### 10.11.24  
- Minor formatting adjustments in `reporting.py` for additional decimal precision.
- Conducted a code review as a group, revisiting each step and verifying the overall functionality.

### 11.11.24 
- added header for `trace_file.log` and additionally adjusted `reporting.py` to read new `trace_file.log` accordingly
- Conducted a final code review as a group, revisiting each step and verifying the overall functionality.