from bank import value

def test_value_hello():
    assert value("Hello") == 0

def test_value_hWord():
    assert value("Hi") == 20

def test_value_word():
    assert value("welcome") == 100
