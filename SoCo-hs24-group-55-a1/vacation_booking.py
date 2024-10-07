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

# AdventureTrip

def adventure_trip_calculate_cost(thing):
    if thing["difficulty_level"] == "hard":
        return thing["cost_per_day"] * thing["duration_in_days"] * 2
    return thing["cost_per_day"] * thing["duration_in_days"]

def adventure_trip_describe_package(thing):
    return f"The {thing['duration_in_days']} day long Adventure Trip in {thing['destination']} is considered {thing['difficulty_level']}."

AdventureTrip = {
    "difficulty_level" : None,
    "calculate_cost" : adventure_trip_calculate_cost,
    "describe_package" : adventure_trip_describe_package,
    "_classname" : "AdventureTrip",
    "_parent" : VacationPackage,
}
#Luxury Cruise

def cruise_calculate_cost(thing):
    if thing["has_private_suite"] == True:
        return ((thing["cost_per_day"] * thing["duration_in_days"]) *1.5)
    return thing["cost_per_day"] * thing["duration_in_days"]

def cruise_describe_package(thing):
    if thing["has_private_suite"] == True:
        return f"The {thing['duration_in_days']} day long Luxury Cruise vacation in {thing['destination']} includes a private Suite."
    return f"The {thing['duration_in_days']} day long Luxury Cruise vacation in {thing['destination']} does not include a private Suite."  

                  
Luxury_Cruise = {
    "has_private_suite": None,
    "calculate_cost" : cruise_calculate_cost,
    "describe_package" : cruise_describe_package,
    "_classname":"Luxury_Cruise",
    "_parent":VacationPackage
}

