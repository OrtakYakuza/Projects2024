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
                 
Beach_Resort = {
    "includes_surfing": False,
    "calculate cost" : beach_resort_calculate_cost,
    "describe package" : beach_resort_describe_package,
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
    "calculate_cost" : cruise_calculate_cost,
    "describe_package" : cruise_describe_package,
    "_classname":"LuxuryCruise",
    "_parent":VacationPackage
}

beach_resort = make(BeachResort, "Maldives", 100, 7, True)
adventure_trip = make(AdventureTrip, "Macchu Picchu", 150, 4, "easy")
luxury_cruise = make(LuxuryCruise, "Mediterranean", 100, 14, False)

>>>>>>> SoCo-hs24-group-55-a1/vacation_booking.py
