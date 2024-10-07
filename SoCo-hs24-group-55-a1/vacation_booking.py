def beach_resort_calculate_cost(thing):
    if thing["includes_surfing"] == True:
        return thing["cost_per_day"] * thing["duration_in_days"] + 100
    return thing["cost_per_day"] * thing["duration_in_days"]

def beach_resort_describe_package(thing):
    if thing["includes_surfing"] == True:
        return f"The thing['duration_in_days'] day long Beach Resort vacation in thing['destination'] includes surfing."
    return f"The thing['duration_in_days'] day long Beach Resort vacation in thing['destination'] does not include surfing."  

                  
Beach_Resort = {
    "includes_surfing": None,
    "calculate cost" : beach_resort_calculate_cost
    "describe package" : beach_resort_describe_package
    "_classname":"BeachResort",
    "_parent":VacationPackage
}