import sys
import time
from vacation_booking import BeachResort, AdventureTrip, LuxuryCruise, make, call
from colorama import Fore, Style


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
invalid_package = make(what, "Panama", 100, 0, True)

def setUp():
    global beach_resort_without_surfing, beach_resort_with_surfing, beach_resort_invalid_location, each_resort_invalid_surfing, adventure_trip_easy, adventure_trip_hard, adventure_trip_negative_cost, adventure_trip_negative_days, luxury_cruise_without_suite, luxury_cruise_with_suite, luxury_cruise_calculate_cost_zero_days, invalid_package

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
    invalid_package = make(what, "Panama", 100, 0, True)

def tearDown():
    global beach_resort_without_surfing, beach_resort_with_surfing, beach_resort_invalid_location, each_resort_invalid_surfing, adventure_trip_easy, adventure_trip_hard, adventure_trip_negative_cost, adventure_trip_negative_days, luxury_cruise_without_suite, luxury_cruise_with_suite, luxury_cruise_calculate_cost_zero_days, invalid_package

    beach_resort_without_surfing = None
    beach_resort_with_surfing = None
    beach_resort_invalid_location = None
    each_resort_invalid_surfing = None
    adventure_trip_easy = None
    adventure_trip_hard = None
    adventure_trip_negative_cost = None
    adventure_trip_negative_days = None
    luxury_cruise_without_suite = None
    luxury_cruise_with_suite = None
    luxury_cruise_calculate_cost_zero_days = None
    invalid_package = None

# tests
def test_beach_resort_calculate_cost_without_surfing():
        expected_result = 500        # 5*100 (basis) 
        actual_result = call(beach_resort_without_surfing, "calculate_cost")
        assert expected_result == actual_result

def test_beach_resort_calculate_cost_with_surfing():
        expected_result = 600     # 5*100 (basis) + 100(surfing)
        actual_result = call(beach_resort_with_surfing, "calculate_cost")
        assert expected_result == actual_result

def test_adventure_trip_calculate_cost_easy():
        expected_result = 500     #5*100 (basis)
        actual_result = call(adventure_trip_easy, "calculate_cost")
        assert expected_result == actual_result

def test_adventure_trip_calculate_cost_hard():
        expected_result = 1000      #(5*100)*2 (basis times two)
        actual_result = call(adventure_trip_hard, "calculate_cost")
        assert expected_result == actual_result

def test_luxury_cruise_calculate_cost_without_suite():
        expected_result = 500       #5*100(basis)
        actual_result = call(luxury_cruise_without_suite, "calculate_cost")
        assert  expected_result == actual_result

def test_luxury_cruise_calculate_with_suite():
        expected_result = 750       #(5*100(basis))*1.5
        actual_result = call(luxury_cruise_with_suite, "calculate_cost")
        assert  expected_result == actual_result

def test_beach_resort_describe_package_without_surfing():
        expected_result = "The 5 day long Beach Resort vacation in Bosnia does not include surfing."
        actual_result = call(beach_resort_without_surfing, "describe_package")
        assert expected_result == actual_result

def test_beach_resort_describe_package_with_surfing():
        expected_result = "The 5 day long Beach Resort vacation in Bosnia includes surfing."
        actual_result = call(beach_resort_with_surfing, "describe_package")
        assert expected_result == actual_result

def test_adventure_trip_describe_package_easy():
        expected_result = "The 5 day long Adventure Trip in Indonesia is considered easy."
        actual_result = call(adventure_trip_easy, "describe_package")
        assert expected_result == actual_result

def test_adventure_trip_describe_package_hard():
        expected_result = "The 5 day long Adventure Trip in Indonesia is considered hard."
        actual_result = call(adventure_trip_hard, "describe_package")
        assert expected_result == actual_result

def test_luxury_cruise_describe_package_without_suite():
        expected_result = "The 5 day long Luxury Cruise vacation in Panama does not include a private Suite."
        actual_result = call(luxury_cruise_without_suite, "describe_package")
        assert expected_result == actual_result

def test_luxury_cruise_describe_package_with_suite():
        expected_result = "The 5 day long Luxury Cruise vacation in Panama includes a private Suite."
        actual_result = call(luxury_cruise_with_suite, "describe_package")
        assert expected_result == actual_result

#VactionBookingSummary Tests

def test_vacation_booking_summary_totalcost():
        summary = make_vacation_booking_summary()  
        total_cost = summary["calculate_total_cost"]()
        expected_total_cost = 2350
        assert total_cost == expected_total_cost

def test_vacation_booking_summary():
        summary = make_vacation_booking_summary()  
        vacation_summary = summary["extract_total_vacation_summary"]()
        expected_summary = 
            ["The 5 day long Beach Resort vacation in Bosnia includes surfing.",
            "The 5 day long Adventure Trip in Indonesia is considered hard.",
            "The 5 day long Luxury Cruise vacation in Panama includes a private Suite."]
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
    assert total_cost == expected_total_cost, f"Expected total cost to be {expected_total_cost}, but got {total_cost}"

def test_vacation_booking_summary_empty():
    summary = make_vacation_booking_summary()
    vacation_summary = summary["extract_total_vacation_summary"]()
    expected_summary = []
    assert vacation_summary == expected_summary, f"Expected summary to be {expected_summary}, but got {vacation_summary}"

def test_adventure_trip_negative_cost():
    try:
        adventure_trip_negative_cost = make(AdventureTrip, "Indonesia", -500, 5, "hard")
        assert False, "Expected ValueError due to negative cost, but no error was raised"
    except ValueError:
        assert True
    except Exception as e:
        assert False, f"Unexpected exception raised: {e}"


def test_adventure_trip_negative_days():
    try:
        adventure_trip_negative_days = make(AdventureTrip, "Himalayas", 150, -3, "easy")
        assert False, "Expected ValueError due to negative days, but no error was raised"
    except ValueError:
        assert True 
    except Exception as e:
        assert False, f"Unexpected exception raised: {e}"

def test_beach_resort_invalid_surfing():
    try:
        beach_resort_invalid_surfing = make(BeachResort, "Maldives", 200, 7, "what")
        assert False, "Expected ValueError due to invalid surfing parameter, but no error was raised"
    except ValueError:
        assert True  
    except Exception as e:
        assert False, f"Unexpected exception raised: {e}"

def test_luxury_cruise_zero_days():
    try:
        luxury_cruise_calculate_cost_zero_days = make(LuxuryCruise, "Caribbean", 300, 0, True)
        assert False, "Expected ValueError due to zero days, but no error was raised"
    except ValueError:
        assert True  
    except Exception as e:
        assert False, f"Unexpected exception raised: {e}"

def test_beach_resort_invalid_location():
    try:
        beach_resort_invalid_location = make(BeachResort, 5, 800, 4, True)
        assert False, "Expected ValueError due to invalid location, but no error was raised"
    except ValueError:
        assert True  
    except Exception as e:
        assert False, f"Unexpected exception raised: {e}"

def test_invalid_package():
    try:
        invalid_package = make(Hello, 3, 700, 5, True)
        assert False, "Expected NameError due to invalid package, but no error was raised"
    except NameError:
        assert True 
    except Exception as e:
        assert False, f"Unexpected exception raised: {e}"

def test_invalid_searchterm():
    try:
        make_vacation_booking_summary(search_term="idontknow")
        assert False, "Expected ValueError due to invalid search term, but no error was raised"
    except ValueError:
        assert True 
    except Exception as e:
        assert False, f"Unexpected exception raised: {e}"

# run all tests
def run_tests():
    results = {"pass": 0, "fail": 0, "error": 0}
    print(f"{Style.BRIGHT}{Fore.CYAN}\n{'-'*30}\nRunning Tests\n{'-'*30}{Style.RESET_ALL}")
    for (name, test) in globals().items():
        if not name.startswith("test_"):
            continue
        start_time = time.time() #für farben (colorama) library Ai zur unterstützung genutzt (README.md ergänzen)
        setUp()                        
        try:
            test()
            results["pass"] += 1
            print(f"{Fore.GREEN}{name}: pass{Style.RESET_ALL} ({time.time() - start_time:.2f} seconds)")
        except AssertionError:
            results["fail"] += 1
            print(f"{Fore.RED}{name}: fail{Style.RESET_ALL} ({time.time() - start_time:.2f} seconds)")
        except Exception as error:
            results["error"] += 1
            print(f"{Fore.YELLOW}{name}: error{Style.RESET_ALL} ({time.time() - start_time:.2f} seconds) - {error}")
        tearDown()
    print(f"{Style.BRIGHT}{Fore.CYAN}\n{'-'*30}\nSummary\n{'-'*30}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}pass: {results['pass']}{Style.RESET_ALL}")
    print(f"{Fore.RED}fail: {results['fail']}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}error: {results['error']}{Style.RESET_ALL}")

# main function
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--select":
        select_pattern = sys.argv[2]
    else:
        select_pattern = None
    run_tests()

