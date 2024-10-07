def calculate_cost(thing):
    if thing["includes_surfing"] == True:
        return thing["cost_per_day"] * thing["duration_in_days"] + 100
    return thing["cost_per_day"] * thing["duration_in_days"]

def describe_package(thing):
    if thing["includes_surfing"] == True:
        return f"The thing['duration_in_days'] day long Beach Resort vacation in thing['destination'] includes surfing."
    return f"The thing['duration_in_days'] day long Beach Resort vacation in thing['destination'] does not include surfing."  

                  
Beach_Resort = {
    "includes_surfing": None,
    "_classname":"BeachResort",
    "_parent":VacationPackage
}