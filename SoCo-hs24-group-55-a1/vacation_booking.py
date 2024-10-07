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
    "describe_package" : describe_package,
    "_classname" : "VacationPackage",
    "_parent": None,
}

import math


def calculate_cost(thing):
    raise NotImplementedError("Method has not been Implemented")

def describe_package(thing):
    raise NotImplementedError("Method has not been Implemented")


VacationPackage = {
    "destination" : None,
    "cost_per_day" : None,
    "duration_in_days" : None,
    "calculate_cost" : calculate_cost,
    "_classname" : "VacationPackage",
    "_parent": None,
}

def calculate_cost(thing):
    if thing["includes_surfing"] == True:
        return BeachResort["cost_per_day"] * thing["duration_in_days"] + 100
    thing["cost_per_day"] * thing["duration_in_days"]

def describe_package(thing):
    if thing["includes_surfing"] == True:
        return f"The thing['duration_in_days'] day long Beach Resort vacation in thing['destination'] includes surfing."
    return f"The thing['duration_in_days'] day long Beach Resort vacation in thing['destination'] does not include surfing."  

                  
Beach_Resort = {
    "includes_surfing": None,
    "_classname":"BeachResort",
    "_parent":VacationPackage
}