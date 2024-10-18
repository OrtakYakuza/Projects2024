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