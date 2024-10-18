def test_vacation_booking_summary_totalcost():
        summary = make_vacation_booking_summary()  
        total_cost = summary["calculate_total_cost"]()
        expected_total_cost = 300
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
        expected_total_cost = 100
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
   

