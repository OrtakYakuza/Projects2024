import sys
import time
from vacation_booking import BeachResort, AdventureTrip, LuxuryCruise, make, call

beach_resort_without_surfing = make(BeachResort, "Bosnia", 100, 5, False)
beach_resort_with_surfing = make(BeachResort, "Bosnia", 100, 5, True)
beach_resort_invalid_location = make(BeachResort, 5, 100, 5, True)
each_resort_invalid_surfing = make(BeachResort, "Bosnia", 100, 5, 0)
adventure_trip_easy = make(AdventureTrip, "Indonesia", 100, 5, "easy")
adventure_trip_hard = make(AdventureTrip, "Indonesia", 100, 5, "hard")
adventure_trip_negative_cost = make(AdventureTrip, "Indonesia", -100, 5, "hard")
adventure_trip_negative_days = make(AdventureTrip, "Indonesia", 100, -5, "hard")
luxury_cruise_without_suite = make(LuxuryCruise, "Panama", 100, 5, False)
luxury_cruise_with_suite = make(LuxuryCruise, "Panama", 100, 5, True)
luxury_cruise_calculate_cost_zero_days = make(LuxuryCruise, "Panama", 100, 0, True)
invalid_package = make("Surfing", "Panama", 100, 0, True)

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

#VactionBookingSummary Tests

def test_vacation_booking_summary_totalcost():
        summary = make_vacation_booking_summary()  
        total_cost = summary["calculate_total_cost"]()
        expected_total_cost = 2350
        assert total_cost == expected_total_cost

def test_vacation_booking_summary():
        summary = make_vacation_booking_summary()  
        vacation_summary = summary["extract_total_vacation_summary"]()
        expected_summary = [
            "The 5 day long Beach Resort vacation in Bosnia includes surfing.",
            "The 5 day long Adventure Trip in Indonesia is considered hard.",
            "The 5 day long Luxury Cruise vacation in Panama includes a private Suite."
        ]
        assert vacation_summary == expected_summary


def test_vacation_booking_summary_AdventureTrip_totalcost():
        summary = make_vacation_booking_summary("AdventureTrip")
        total_cost = summary["calculate_total_cost"]()
        expected_total_cost = 1000
        assert total_cost == expected_total_cost

def test_vacation_booking_summary_AdventureTrip():
        summary = make_vacation_booking_summary("AdventureTrip")
        vacation_summary = summary["extract_total_vacation_summary"]()
        expected_summary = ["The 5 day long Adventure Trip in Indonesia is considered hard."]
        assert vacation_summary == expected_summary


def test_vacation_booking_summary_BeachResort_totalcost():
        summary = make_vacation_booking_summary("BeachResort")
        total_cost = summary["calculate_total_cost"]()
        expected_total_cost = 600
        assert total_cost == expected_total_cost


def test_vacation_booking_summary_BeachResort():
        summary = make_vacation_booking_summary("BeachResort")
        vacation_summary = summary["extract_total_vacation_summary"]()
        expected_summary = ["The 5 day long Beach Resort vacation in Bosnia includes surfing."]
        assert vacation_summary == expected_summary


def test_vacation_booking_summary_LuxuryCruise_totalcost():
        summary = make_vacation_booking_summary("LuxuryCruise")
        total_cost = summary["calculate_total_cost"]()
        expected_total_cost = 750
        assert total_cost == expected_total_cost
   

def test_vacation_booking_summary_LuxuryCruise():
        summary = make_vacation_booking_summary("LuxuryCruise")
        vacation_summary = summary["extract_total_vacation_summary"]()
        expected_summary = ["The 5 day long Luxury Cruise vacation in Panama includes a private Suite."]
        assert vacation_summary == expected_summary

#EdgeCases
def test_vacation_booking_summary_empty_totalcost():
    summary = make_vacation_booking_summary()
    total_cost = summary["calculate_total_cost"]()
    expected_total_cost = 0
    assert total_cost == expected_total_cost

def test_vacation_booking_summary_empty():
        summary = make_vacation_booking_summary()
        vacation_summary = summary["extract_total_vacation_summary"]()
        expected_summary = []
        assert vacation_summary == expected_summary

def test_adventure_trip_calculate_cost_negative_cost():
    expected_result = ValueError    
    actual_result = call(adventure_trip_negative_cost, "calculate_cost")
    assert expected_result == actual_result

def test_adventure_trip_calculate_cost_negative_days():
    expected_result = ValueError    
    actual_result = call(adventure_trip_negative_days, "calculate_cost")
    assert expected_result == actual_result

def test_beach_resort_invalid_surfing():
    expected_result = ValueError    
    actual_result = call(beach_resort_invalid_surfing, "calculate_cost")
    assert expected_result == actual_result

def test_luxury_cruise_calculate_cost_zero_days():
    expected_result = ValueError    
    actual_result = call(luxury_cruise_calculate_cost_zero_days, "calculate_cost")
    assert expected_result == actual_result

def test_beach_resort_invalid_location():
     expected_result = ValueError
    actual_result = call(beach_resort_invalid_location, "describe_package")
    assert expected_result == actual_result

def test_invalid_package():
     expected_result = ValueError
    actual_result = call(invalid_package, "describe_package")
    assert expected_result == actual_result




def run_tests():
    results = {"pass": 0, "fail": 0, "error": 0}
    for (name, test) in globals().items():
        if not name.startswith("test_"):
            continue
        if select_pattern and select_pattern not in name:
            continue
        try:
            test()
            results["pass"] += 1
        except AssertionError:
            results["fail"] += 1
        except Exception:
            results["error"] += 1
    print(f"pass {results['pass']}")
    print(f"fail {results['fail']}")
    print(f"error {results['error']}")

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--select":
        select_pattern = sys.argv[2]
    else:
        select_pattern = None
    run_tests()
>>>>>>> SoCo-hs24-group-55-a1/test_vacation_booking.py
