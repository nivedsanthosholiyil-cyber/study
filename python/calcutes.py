from calcu import squre

def test_positive():
    assert squre(2) == 4
    assert squre(3) == 9

def test_negative():
    assert squre(-2) == 4
    assert squre(-3) == 9
    assert squre(-4) == 16

def test_zero():
    assert squre(0) == 0