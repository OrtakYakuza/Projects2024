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

#find/call function

def call(thing, key_name, *args):
    method = find(thing["_class"], key_name)
    return method(thing, *args)

def find(cls, key_name):
    if key_name in cls:
        return cls[key_name]
    if cls["_parent"]:
        return find(cls["_parent"], key_name)
    raise NotImplementedError("Missing method " + key_name)

# make function
Booked_Holidays = []

def make(package, destination, cost_per_day, duration_in_days, *args):
    if not isinstance(destination, str):
        raise ValueError("Destination must be a string")
    if cost_per_day < 0:
        raise ValueError("Cost per day cannot be negative")
    if duration_in_days <= 0:
        raise ValueError("Duration must be greater than zero")

    if package == BeachResort:
        includes_surfing = args[0]
        if not isinstance(includes_surfing, bool):
            raise ValueError("Includes_surfing must be a boolean")
        new_thing = {
            "destination" : destination,
            "cost_per_day" : cost_per_day,
            "duration_in_days" : duration_in_days,
            "includes_surfing" : includes_surfing,
            "_class" : BeachResort}
        Booked_Holidays.append(new_thing)
        return new_thing
    elif package == AdventureTrip:
        difficulty_level = args[0]
        if difficulty_level not in ["easy", "hard"]:
            raise ValueError("Invalid difficulty level")
        new_thing = {
            "destination" : destination,
            "cost_per_day" : cost_per_day,
            "duration_in_days" : duration_in_days,
            "difficulty_level" : difficulty_level,
            "_class" : AdventureTrip}
        Booked_Holidays.append(new_thing)
        return new_thing
    elif package == LuxuryCruise:
        has_private_suite = args[0]
        if not isinstance(has_private_suite, bool):
            raise ValueError("has_private_suite must be a boolean")
        new_thing = {
            "destination" : destination,
            "cost_per_day" : cost_per_day,
            "duration_in_days" : duration_in_days,
            "has_private_suite" : has_private_suite,
            "_class" : LuxuryCruise}
        Booked_Holidays.append(new_thing)
        return new_thing
    else:
        raise ValueError("Package is nonexistent")

beach_resort1 = make(BeachResort, "Maldives", 100, 7, True)
adventure_trip1 = make(AdventureTrip, "Macchu Picchu", 150, 4, "easy")  #these are in the Booked_holidays List
luxury_cruise1 = make(LuxuryCruise, "Mediterranean", 100, 14, True)

def calculate_total_cost():
    total_price = []
    if VacationBookingSummary["search_term"] is None:
        for booking in Booked_Holidays:
            total_price.append(call(booking,"calculate_cost"))
        return sum(total_price)
    else:
        for booking in Booked_Holidays:
            if VacationBookingSummary["search_term"].lower() in booking["_class"]["_classname"].lower():
                total_price.append(call(booking,"calculate_cost"))
        return sum(total_price)


def extract_total_vacation_summary():
    Summary = []
    if VacationBookingSummary["search_term"] is None:
        for booking in Booked_Holidays:
            Summary.append(call(booking,"describe_package"))
        return Summary
    else:
        for booking in Booked_Holidays:
            if VacationBookingSummary["search_term"].lower() in booking["_class"]["_classname"].lower():
                Summary.append(call(booking,"describe_package"))
        return Summary
        
VacationBookingSummary = {
    "search_term" : None
}


def make_vacation_booking_summary(search_term=None):
    VacationBookingSummary["search_term"] = search_term 
    return {
        "search_term": search_term,
        "calculate_total_cost": calculate_total_cost,
        "extract_total_vacation_summary": extract_total_vacation_summary
    }




