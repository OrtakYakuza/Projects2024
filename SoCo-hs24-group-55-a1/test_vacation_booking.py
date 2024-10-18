import time
from vacation_booking import BeachResort, AdventureTrip, LuxuryCruise, make, call

beach_resort_without_surfing = make(BeachResort, "Bosnia", 100, 5, False)
beach_resort_with_surfing = make(BeachResort, "Bosnia", 100, 5, True)
adventure_trip_easy = make(AdventureTrip, "Indonesia", 100, 5, "easy")
adventure_trip_hard = make(AdventureTrip, "Indonesia", 100, 5, "hard")
luxury_cruise_without_suite = make(LuxuryCruise, "Panama", 100, 5, False)
luxury_cruise_with_suite = make(LuxuryCruise, "Panama", 100, 5, True)

def test_beach_resort_calculate_cost_without_surfing():
    try: 
        expected_result = 500        # 5*100 (basis) 
        actual_result = call(beach_resort_without_surfing, "calculate_cost")
        assert expected_result == actual_result
        print(f"test_beach_resort_calculate_cost_without_surfing: pass")
    except AssertionError:
        print(f"test_beach_resort_calculate_cost_without_surfing: fail")
    except Exception:
        print(f"test_beach_resort_calculate_cost_without_surfing: error")

def test_beach_resort_calculate_cost_with_surfing():
    try: 
        expected_result = 600     # 5*100 (basis) + 100(surfing)
        actual_result = call(beach_resort_with_surfing, "calculate_cost")
        assert expected_result == actual_result
        print(f"test_beach_resort_calculate_cost_with_surfing: pass")
    except AssertionError:
        print(f"test_beach_resort_calculate_cost_with_surfing: fail")
    except Exception:
        print(f"test_beach_resort_calculate_cost_with_surfing: error")

def test_adventure_trip_calculate_cost_easy():
    try:
        expected_result = 500     #5*100 (basis)
        actual_result = call(adventure_trip_easy, "calculate_cost")
        assert expected_result == actual_result
        print(f"test_adventure_trip_calculate_cost_easy: pass")
    except AssertionError:
        print(f"test_adventure_trip_calculate_cost_easy: fail")
    except Exception:
        print(f"test_adventure_trip_calculate_cost_easy: error")

def test_adventure_trip_calculate_cost_hard():
    try:
        expected_result = 1000      #(5*100)*2 (basis times two)
        actual_result = call(adventure_trip_hard, "calculate_cost")
        assert expected_result == actual_result
        print(f"test_adventure_trip_calculate_cost_hard: pass")
    except AssertionError:
        print(f"test_adventure_trip_calculate_cost_hard: fail")
    except Exception:
        print(f"test_adventure_trip_calculate_cost_hard: error")

def test_luxury_cruise_calculate_cost_without_suite():
    try:
        expected_result = 500       #5*100(basis)
        actual_result = call(luxury_cruise_without_suite, "calculate_cost")
        assert  expected_result == actual_result
        print(f"test_luxury_cruise_calculate_cost_without_suite: pass")
    except AssertionError:
        print(f"test_luxury_cruise_calculate_cost_without_suite: fail")
    except Exception:
        print(f"test_luxury_cruise_calculate_cost_without_suite: error")

def test_luxury_cruise_calculate_with_suite():
    try:
        expected_result = 750       #(5*100(basis))*1.5
        actual_result = call(luxury_cruise_with_suite, "calculate_cost")
        assert  expected_result == actual_result
        print(f"test_luxury_cruise_calculate_with_suite: pass")
    except AssertionError:
        print(f"test_luxury_cruise_calculate_with_suite: fail")
    except Exception:
        print(f"test_luxury_cruise_calculate_with_suite: error")

def test_beach_resort_describe_package_without_surfing():
    try:
        expected_result = "The 5 day long Beach Resort vacation in 'Bosnia' does not include surfing."
        actual_result = call(beach_resort_without_surfing, "describe_package")
        assert expected_result == actual_result
        print("test_beach_resort_describe_package_without_surfing: pass")
    except AssertionError:
        print("test_beach_resort_describe_package_without_surfing: fail")
    except Exception:
        print("test_beach_resort_describe_package_without_surfing: error")

def test_beach_resort_describe_package_with_surfing():
    try:
        expected_result = "The 5 day long Beach Resort vacation in 'Bosnia' includes surfing."
        actual_result = call(beach_resort_with_surfing, "describe_package")
        assert expected_result == actual_result
        print("test_beach_resort_describe_package_with_surfing: pass")
    except AssertionError:
        print("test_beach_resort_describe_package_with_surfing: fail")
    except Exception:
        print("test_beach_resort_describe_package_with_surfing: error")

def test_adventure_trip_describe_package_easy():
    try:
        expected_result = "The 5 day long Adventure Trip in 'Indonesia' is considered easy."
        actual_result = call(adventure_trip_easy, "describe_package")
        assert expected_result == actual_result
        print("test_adventure_trip_describe_package_easy: pass")
    except AssertionError:
        print("test_adventure_trip_describe_package_easy: fail")
    except Exception:
        print("test_adventure_trip_describe_package_easy: error")

def test_adventure_trip_describe_package_hard():
    try:
        expected_result = "The 5 day long Adventure Trip in 'Indonesia' is considered hard."
        actual_result = call(adventure_trip_hard, "describe_package")
        assert expected_result == actual_result
        print("test_adventure_trip_describe_package_hard: pass")
    except AssertionError:
        print("test_adventure_trip_describe_package_hard: fail")
    except Exception:
        print("test_adventure_trip_describe_package_hard: error")

def test_luxury_cruise_describe_package_without_suite():
    try:
        expected_result = "The 5 day long Luxury Cruise vacation in 'Panama' does not include a private Suite."
        actual_result = call(luxury_cruise_without_suite, "describe_package")
        assert expected_result == actual_result
        print("test_luxury_cruise_describe_package_without_suite: pass")
    except AssertionError:
        print("test_luxury_cruise_describe_package_without_suite: fail")
    except Exception:
        print("test_luxury_cruise_describe_package_without_suite: error")

def test_luxury_cruise_describe_package_with_suite():
    try:
        expected_result = "The 5 day long Luxury Cruise vacation in 'Panama' includes a private Suite."
        actual_result = call(luxury_cruise_with_suite, "describe_package")
        assert expected_result == actual_result
        print("test_luxury_cruise_describe_package_with_suite: pass")
    except AssertionError:
        print("test_luxury_cruise_describe_package_with_suite: fail")
    except Exception:
        print("test_luxury_cruise_describe_package_with_suite: error")
