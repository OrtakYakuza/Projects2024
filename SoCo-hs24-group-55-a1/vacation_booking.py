# make function

def make(package, destination, cost_per_day, duration_in_days, *args):
    if package == BeachResort:
        includes_surfing = args[0]
        new_thing = {
            "destination" : destination,
            "cost_per_day" : cost_per_day,
            "duration_in_days" : duration_in_days,
            "includes_surfing" : includes_surfing,
            "_class" : BeachResort}
        return new_thing
    elif package == AdventureTrip:
        difficulty_level = args[0]
        new_thing = {
            "destination" : destination,
            "cost_per_day" : cost_per_day,
            "duration_in_days" : duration_in_days,
            "difficulty_level" : difficulty_level,
            "_class" : AdventureTrip}
        return new_thing
    elif package == LuxuryCruise:
        pass
    else:
        raise ValueError("Package is nonexistent")