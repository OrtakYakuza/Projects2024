import math

# abstract methods of the parent class

def calculate_cost(thing):
    raise NotImplementedError("Method has not been Implemented")

def describe_package(thing):
    raise NotImplementedError("Method has not been Implemented")

# parent class

VacationPackage = {
    "destination" : None,
    "cost_per_day" : None,
    "duration_in_days" : None,
    "calculate_cost" : calculate_cost,
    "duration_in_days" : duration_in_days,
    "_classname" : "VacationPackage",
    "_parent": None,
}

# make function

def make(package, destination, cost_per_day, duration_in_days, *args):
    if package == BeachResort:
        pass
    elif package == AdventureTrip:
        pass
    elif package == LuxuryCruise:
        pass
    else:
        raise ValueError("Package is nonexistent")