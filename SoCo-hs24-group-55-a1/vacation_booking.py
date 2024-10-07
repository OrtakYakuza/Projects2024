import math

# abstract methods of the parent class

def calculate_cost(thing):
    raise NotImplementedError("Method has not been Implemented")

def duration_in_days(thing):
    raise NotImplementedError("Method has not been Implemented")

# parent class

VacationPackage = {
    "destination" : None,
    "cost_per_day" : None,
    "duration_in_days" : None,
    "calculate_cost" : calculate_cost(),
    "duration_in_days" : duration_in_days(),
    "_classname" : "VacationPackage",
    "_parent": None,
}