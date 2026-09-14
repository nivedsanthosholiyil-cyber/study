from back import value

def test_hello():
    assert value("hello ") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0

def test_h():
    assert value ("h") == 0

def test_other():
    assert value ("good morning") == 0