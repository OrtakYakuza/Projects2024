def test_vacation_booking_summary():
    try:

        summary = make_vacation_booking_summary()  
        total_cost = summary["calculate_total_cost"]()
        expected_total_cost = 1400
        assert total_cost == expected_total_cost, f"Expected {expected_total_cost}, but got {total_cost}"
    except AssertionError as e:
        print(f"test_vacation_booking_summary: fail - {e}")
    except Exception as e:
        print(f"test_vacation_booking_summary: exception - {e}")

    try:
        vacation_summary = summary.extract_total_vacation_summary()  
        expected_summary = [
            "The 7 day long Beach Resort vacation in Maldives includes surfing.",
            "The 4 day long Adventure Trip in Berlin is considered easy.",
            "The 14 day long Luxury Cruise vacation in Bali includes a private Suite."
        ]
        assert vacation_summary == expected_summary, f"Expected {expected_summary}, but got {vacation_summary}"
    except AssertionError as e:
        print(f"test_vacation_booking_summary_AdventureTrip: fail - {e}")
    except Exception as e:
        print(f"test_vacation_booking_summary_AdventureTrip: exception - {e}")




def test_vacation_booking_summary_AdventureTrip():
    try:
        summary = make_vacation_booking_summary("AdventureTrip")
        total_cost = summary["calculate_total_cost"]()
        expected_total_cost = 200
        assert total_cost == expected_total_cost, f"Expected {expected_total_cost}, got {total_cost}"
    except AssertionError as e:
        print(f"test_vacation_booking_summary_AdventureTrip: fail - {e}")
    except Exception as e:
        print(f"test_vacation_booking_summary_AdventureTrip: exception - {e}")

    try:
        vacation_summary = summary.extract_total_vacation_summary()
        expected_summary = ["The 4 day long Adventure Trip vacation in Berlin is considered easy."]
        assert vacation_summary == expected_summary, f"Expected {expected_summary}, got {vacation_summary}"
    except AssertionError as e:
        print(f"test_vacation_booking_summary_AdventureTrip: fail - {e}")
    except Exception as e:
        print(f"test_vacation_booking_summary_AdventureTrip: exception - {e}")


def test_vacation_booking_summary_BeachResort():
    try:
        summary = make_vacation_booking_summary("BeachResort")
        total_cost = summary["calculate_total_cost"]()
        expected_total_cost = 600
        assert total_cost == expected_total_cost, f"Expected {expected_total_cost}, got {total_cost}"
    except AssertionError as e:
        print(f"test_vacation_booking_summary_BeachResort: fail - {e}")
    except Exception as e:
        print(f"test_vacation_booking_summary_BeachResort: exception - {e}")

    try:
        vacation_summary = summary.extract_total_vacation_summary()
        expected_summary = ["The 7 day long Beach Resort vacation in Maldives includes surfing."]
        assert vacation_summary == expected_summary, f"Expected {expected_summary}, got {vacation_summary}"
    except AssertionError as e:
        print(f"test_vacation_booking_summary_BeachResort: fail - {e}")
    except Exception as e:
        print(f"test_vacation_booking_summary_BeachResort: exception - {e}")


def test_vacation_booking_summary_LuxuryCruise():
    try:
        summary = make_vacation_booking_summary("LuxuryCruise")
        total_cost = summary["calculate_total_cost"]()
        expected_total_cost = 600
        assert total_cost == expected_total_cost, f"Expected {expected_total_cost}, got {total_cost}"
    except AssertionError as e:
        print(f"test_vacation_booking_summary_LuxuryCruise: fail - {e}")
    except Exception as e:
        print(f"test_vacation_booking_summary_LuxuryCruise: exception - {e}")

    try:
        vacation_summary = summary.extract_total_vacation_summary()
        expected_summary = ["The 10 day long Luxury Cruise vacation in Bali includes a private Suite."]
        assert vacation_summary == expected_summary, f"Expected {expected_summary}, got {vacation_summary}"
    except AssertionError as e:
        print(f"test_vacation_booking_summary_LuxuryCruise: fail - {e}")
    except Exception as e:
        print(f"test_vacation_booking_summary_LuxuryCruise: exception - {e}")