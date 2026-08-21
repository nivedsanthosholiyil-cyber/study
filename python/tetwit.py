from twttr import shorten

def test_lowercase():
    assert shorten("aeiou") == ""

def test_uppercase():
    assert shorten("AEIOU") == ""