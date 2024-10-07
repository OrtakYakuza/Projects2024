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

# AdventureTrip

def calculate_cost(thing):
    if thing["difficulty_level"] == "hard":
        return thing["cost_per_day"] * thing["duration_in_days"] * 2
    return thing["cost_per_day"] * thing["duration_in_days"]

def describe_package(thing):
    return f"The {thing['duration_in_days']} day long Adventure Trip in {thing['destination']} is considered {thing['difficulty_level']}."

AdventureTrip = {
    "difficulty_level" : None
    "_classname" : "AdventureTrip",
    "_parent" : VacationPackage

}