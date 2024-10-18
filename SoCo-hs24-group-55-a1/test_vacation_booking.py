import time
from vacation_booking_vers2 import BeachResort, AdventureTrip, LuxuryCruise, make, call

beach_resort_with_surfing = make(BeachResort, "Bosnia", 100, 5, True)
beach_resort_without_surfing = make(BeachResort, "Bosnia", 100, 5, False)

def test__beach_resort_surfing_calculate_cost():
    try: 
        expected_cost = 600        # 5*100 (basis) + 100(surfing)
        calculated_cost = call(beach_resort_with_surfing, "calculate_cost")
        assert expected_cost == calculated_cost
        print(f"test__beach_resort_surfing_calculate: pass")
    except AssertionError:
        print(f"test__beach_resort_surfing_calculate_cost: fail")
    except Exception:
        print(f"test__beach_resort_surfing_calculate_cost: error")


def test__beach_resort_no_surfing_calculate_cost():
    try: 
        expected_cost = 500        # 5*100 (basis) 
        calculated_cost = call(beach_resort_without_surfing, "calculate_cost")
        assert expected_cost == calculated_cost
        print(f"test__beach_resort_no_surfing_calculate: pass")
    except AssertionError:
        print(f"test__beach_resort_no_surfing_calculate_cost: fail")
    except Exception:
        print(f"test__beach_resort_no_surfing_calculate_cost: error")

adventure_trip_easy = make(AdventureTrip, "Indonesia", 100, 5, "easy")
adventure_trip_hard = make(AdventureTrip, "Indonesia", 100, 5, "hard")

def test_easy_adventure_trip_cost():
    try:
        expected_cost = 500     #5*100 (basis)
        calculated_cost = call(adventure_trip_easy, "calculate_cost")
        assert expected_cost == calculated_cost
        print(f"test_easy_adventure_trip_cost: pass")
    except AssertionError:
        print(f"test_easy_adventure_trip_cost: fail")
    except Exception:
        print(f"test_easy_adventure_trip_cost: error")

def test_hard_adventure_trip_cost():
    try:
        expected_cost = 1000      #(5*100)*2 (basis times two)
        calculated_cost = call(adventure_trip_hard, "calculate_cost")
        assert expected_cost == calculated_cost
        print(f"test_hard_adventure_trip_cost: pass")
    except AssertionError:
        print(f"test_hard_adventure_trip_cost: fail")
    except Exception:
        print(f"test_hard_adventure_trip_cost: error")

luxury_cruise_without_suite = make(LuxuryCruise, "Panama", 100, 5, False)
luxury_cruise_with_suite = make(LuxuryCruise, "Panama", 100, 5, True)

def test_luxury_cruise_without_suite_cost():
    try:
        expected_cost = 500       #5*100(basis)
        calculated_cost = call(luxury_cruise_without_suite, "calculate_cost")
        assert  expected_cost == calculated_cost
        print(f"test_luxury_cruise_without_suite_cost: pass")
    except AssertionError:
        print(f"test_luxury_cruise_without_suite_cost: fail")
    except Exception:
        print(f"test_luxury_cruise_without_suite_cost: error")

def test_luxury_cruise_with_suite_cost():
    try:
        expected_cost = 750       #(5*100(basis))*1.5
        calculated_cost = call(luxury_cruise_with_suite, "calculate_cost")
        assert  expected_cost == calculated_cost
        print(f"test_luxury_cruise_with_suite_cost: pass")
    except AssertionError:
        print(f"test_luxury_cruise_with_suite_cost: fail")
    except Exception:
        print(f"test_luxury_cruise_with_suite_cost: error")

def test_beach_resort_describe_package_with_surfing():
    try:
        expected_result = f"The {thing['duration_in_days']} day long Beach Resort vacation in {thing['destination']} includes surfing."
        actual_result = call(beach_resort, "describe_package")
        assert expected_result == actual_result
        print("test_beach_resort_describe_package_with_surfing: pass")
    except AssertionError:
        print("test_beach_resort_describe_package_with_surfing: fail")
    except Exception:
        print("test_beach_resort_describe_package_with_surfing: error")

def test_beach_resort_describe_package_without_surfing():
    try:
        expected_result = f"The {thing['duration_in_days']} day long Beach Resort vacation in {thing['destination']} does not include surfing."
        actual_result = call(beach_resort, "describe_package")
        assert expected_result == actual_result
        print("test_beach_resort_describe_package_without_surfing: pass")
    except AssertionError:
        print("test_beach_resort_describe_package_without_surfing: fail")
    except Exception:
        print("test_beach_resort_describe_package_without_surfing: error")

def test_adventure_trip_describe_package_easy():
    try:
        expected_result = f"The {thing['duration_in_days']} day long Adventure Trip in {thing['destination']} is considered easy."
        actual_result = call(adventure_trip, "describe_package")
        assert expected_result == actual_result
        print("test_adventure_trip_describe_package_easy: pass")
    except AssertionError:
        print("test_adventure_trip_describe_package_easy: fail")
    except Exception:
        print("test_adventure_trip_describe_package_easy: error")

def test_adventure_trip_describe_package_hard():
    try:
        expected_result = f"The {thing['duration_in_days']} day long Adventure Trip in {thing['destination']} is considered hard."
        actual_result = call(adventure_trip, "describe_package")
        assert expected_result == actual_result
        print("test_adventure_trip_describe_package_hard: pass")
    except AssertionError:
        print("test_adventure_trip_describe_package_hard: fail")
    except Exception:
        print("test_adventure_trip_describe_package_hard: error")

def test_luxury_cruise_describe_package_with_suite():
    try:
        expected_result = f"The {thing['duration_in_days']} day long Luxury Cruise vacation in {thing['destination']} includes a private Suite."
        actual_result = call(luxury_cruise, "describe_package")
        assert expected_result == actual_result
        print("test_luxury_cruise_describe_package_with_suite: pass")
    except AssertionError:
        print("test_luxury_cruise_describe_package_with_suite: fail")
    except Exception:
        print("test_luxury_cruise_describe_package_with_suite: error")

def test_luxury_cruise_describe_package_without_suite():
    try:
        expected_result = f"The {thing['duration_in_days']} day long Luxury Cruise vacation in {thing['destination']} does not include a private Suite."
        actual_result = call(luxury_cruise, "describe_package")
        assert expected_result == actual_result
        print("test_luxury_cruise_describe_package_without_suite: pass")
    except AssertionError:
        print("test_luxury_cruise_describe_package_without_suite: fail")
    except Exception:
        print("test_luxury_cruise_describe_package_without_suite: error")

(test__beach_resort_no_surfing_calculate_cost())
(test__beach_resort_surfing_calculate_cost())
(test_easy_adventure_trip_cost())
(test_hard_adventure_trip_cost())
(test_luxury_cruise_without_suite_cost())
(test_luxury_cruise_with_suite_cost())
