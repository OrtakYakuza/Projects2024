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


(test__beach_resort_no_surfing_calculate_cost())
(test__beach_resort_surfing_calculate_cost())
(test_easy_adventure_trip_cost())
(test_hard_adventure_trip_cost())
(test_luxury_cruise_without_suite_cost())
(test_luxury_cruise_with_suite_cost())