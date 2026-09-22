from 9 import convert


def test_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"


def test_minutes():
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"
    assert convert("12:15 AM to 12:30 PM") == "00:15 to 12:30"


def test_no_minutes():
    assert convert("1 PM to 2 PM") == "13:00 to 14:00"


def test_midnight_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"