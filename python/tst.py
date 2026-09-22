from number import validate
def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("192.168.1.1") == True
    assert validate("255.255.255.255") == True

def test_invalid():
    assert validate("256.0.0.1") == False
    assert validate("192.168.1") == False

def test_non_numeric():
    assert validate("192.168.one.1") == False
    assert validate("abc.def.ghi.jkl") == False

def test_range():
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False