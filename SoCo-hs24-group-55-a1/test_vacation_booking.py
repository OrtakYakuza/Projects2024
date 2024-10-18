def test_vacation_booking_summary_cost():
    try:
        summary = make_vacation_booking_summary()  
        total_cost = summary["calculate_total_cost"]()
        expected_total_cost = 300
        assert total_cost == expected_total_cost

def test_vacation_booking_summary():
    try:
        vacation_summary = summary["extract_total_vacation_summary"]()
        expected_summary = [
            "The 5 day long Beach Resort vacation in Bosnia includes surfing."
            "The 5 day long Adventure Trip in Indonesia is considered hard.",
            "The 5 day long Luxury Cruise vacation in Panama includes a private Suite."
        ]
        assert vacation_summary == expected_summary


def test_vacation_booking_summary_AdventureTrip_totalcost():
    try:
        summary = make_vacation_booking_summary("AdventureTrip")
        total_cost = summary["calculate_total_cost"]()
        expected_total_cost = 100
        assert total_cost == expected_total_cost

def test_vacation_booking_summary_AdventureTrip():
    try:
        vacation_summary = summary["extract_total_vacation_summary"]()
        expected_summary = ["The 5 day long Adventure Trip in Indonesia is considered hard."]
        assert vacation_summary == expected_summary


def test_vacation_booking_summary_BeachResort_totalcost():
    try:
        summary = make_vacation_booking_summary("BeachResort")
        total_cost = summary["calculate_total_cost"]()
        expected_total_cost = 600
        assert total_cost == expected_total_cost


def test_vacation_booking_summary_BeachResort():
    try:
        vacation_summary = summary["extract_total_vacation_summary"]()
        expected_summary = ["The 5 day long Beach Resort vacation in Bosnia includes surfing."]
        assert vacation_summary == expected_summary


def test_vacation_booking_summary_LuxuryCruise_totalcost():
    try:
        summary = make_vacation_booking_summary("LuxuryCruise")
        total_cost = summary["calculate_total_cost"]()
        expected_total_cost = 750
        assert total_cost == expected_total_cost
   

def test_vacation_booking_summary_LuxuryCruise()
    try:
        vacation_summary = summary["extract_total_vacation_summary"]()
        expected_summary = ["The 5 day long Luxury Cruise vacation in Panama includes a private Suite."]
        assert vacation_summary == expected_summary
   

