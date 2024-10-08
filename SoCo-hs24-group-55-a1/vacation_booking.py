import math

#Abstract Methods

def calculate_cost(thing):
    raise NotImplementedError("Method has not been Implemented")

def describe_package(thing):
    raise NotImplementedError("Method has not been Implemented")

#Parent Class

VacationPackage = {
    "destination" : None,
    "cost_per_day" : None,
    "duration_in_days" : None,
    "calculate_cost" : calculate_cost,
    "describe_package" : describe_package,
    "_classname" : "VacationPackage",
    "_parent": None,
}

#BeachResort

def beach_resort_calculate_cost(thing):
    if thing["includes_surfing"] == True:
        return thing["cost_per_day"] * thing["duration_in_days"] + 100
    return thing["cost_per_day"] * thing["duration_in_days"]

def beach_resort_describe_package(thing):
    if thing["includes_surfing"] == True:
        return f"The {thing['duration_in_days']} day long Beach Resort vacation in {thing['destination']} includes surfing."
    return f"The {thing['duration_in_days']} day long Beach Resort vacation in {thing['destination']} does not include surfing."  
                 
BeachResort = {
    "includes_surfing": False,
    "calculate_cost" : beach_resort_calculate_cost,
    "describe_package" : beach_resort_describe_package,
    "_classname":"BeachResort",
    "_parent":VacationPackage
}

#AdventureTrip

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

#LuxuryCruise

def luxury_cruise_calculate_cost(thing):
    if thing["has_private_suite"] == True:
        return ((thing["cost_per_day"] * thing["duration_in_days"]) *1.5)
    return thing["cost_per_day"] * thing["duration_in_days"]

def luxury_cruise_describe_package(thing):
    if thing["has_private_suite"] == True:
        return f"The {thing['duration_in_days']} day long Luxury Cruise vacation in {thing['destination']} includes a private Suite."
    return f"The {thing['duration_in_days']} day long Luxury Cruise vacation in {thing['destination']} does not include a private Suite."  
         
LuxuryCruise = {
    "has_private_suite": None,
    "calculate_cost" : luxury_cruise_calculate_cost,
    "describe_package" : luxury_cruise_describe_package,
    "_classname":"LuxuryCruise",
    "_parent":VacationPackage
}

# make function

def make(package, destination, cost_per_day, duration_in_days, *args):
    if package == BeachResort:
        includes_surfing = args[0]
        new_thing = {
            "destination" : destination,
            "cost_per_day" : cost_per_day,
            "duration_in_days" : duration_in_days,
            "includes_surfing" : includes_surfing,
            "calculate_cost" : beach_resort_calculate_cost,
            "describe_package" : beach_resort_describe_package,
            "_class" : BeachResort}
        return new_thing
    elif package == AdventureTrip:
        difficulty_level = args[0]
        new_thing = {
            "destination" : destination,
            "cost_per_day" : cost_per_day,
            "duration_in_days" : duration_in_days,
            "difficulty_level" : difficulty_level,
            "calculate_cost" : adventure_trip_calculate_cost,
            "describe_package" : adventure_trip_describe_package,
            "_class" : AdventureTrip}
        return new_thing
    elif package == LuxuryCruise:
        has_private_suite = args[0]
        new_thing = {
            "destination" : destination,
            "cost_per_day" : cost_per_day,
            "duration_in_days" : duration_in_days,
            "has_private_suite" : has_private_suite,
            "calculate_cost" : luxury_cruise_calculate_cost,
            "describe_package" : luxury_cruise_describe_package,
            "_class" : LuxuryCruise}
        return new_thing
    else:
        raise ValueError("Package is nonexistent")

# Test Calls

beach_resort = make(BeachResort, "Maldives", 100, 7, True)
adventure_trip = make(AdventureTrip, "Macchu Picchu", 150, 4, "easy")
luxury_cruise = make(LuxuryCruise, "Mediterranean", 100, 14, False)


