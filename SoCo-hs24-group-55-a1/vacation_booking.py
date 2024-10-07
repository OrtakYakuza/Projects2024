##parent class start with initalizing dict 

def init_VacationPackage(Vacation_Destination,cost_per_day,duration_in_days):

    return  {
        "destination" : Vacation_Destination,
        "cost_per_day": cost_per_day, 
        "duration_in_days": duration_in_days,
        "calculate_cost": calculate_cost,
        "describe_package": describe_package
    }

def calculate_cost(vacation):
    return (vacation["cost_per_day"] * vacation["duration_in_days"])                    ##the 2 "base" functions

def describe_package(vacation):
    return f"The {vacation['duration_in_days']} day long xxx in {vacation['destination']} "


def init_LuxuryCruise(Vacation_Destination,cost_per_day,duration_in_days,has_private_suite):

    vacation= init_VacationPackage(Vacation_Destination,cost_per_day,duration_in_days)
    vacation['has_private_suite'] = has_private_suite

    base_calculate_cost = vacation['calculate_cost']  #reference so it doesn't get an recursion error


    def calculate_cost_cruise(vacation):
        Grundkosten = base_calculate_cost(vacation)
        if vacation["has_private_suite"]:
            return  Grundkosten*1.5
        return Grundkosten
    
    base_description = vacation["describe_package"]     #reference so it doesn't get an recursion error
        
    def describe_package_cruise(vacation):
        standart = base_description(vacation)
        
        if vacation['has_private_suite'] == True: 
            suite_description='includes a private suite'
        else:
            suite_description='does not include a private suite'
        
        return standart + suite_description
    
    vacation['calculate_cost'] = calculate_cost_cruise 
    vacation['describe_package'] = describe_package_cruise

    return vacation
    
        


vacation1= init_LuxuryCruise('Maledives', 500, 10, False)


print(vacation1["calculate_cost"](vacation1))
print(vacation1["describe_package"](vacation1))  #name not finished, adjusting with subclass name needed






    