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