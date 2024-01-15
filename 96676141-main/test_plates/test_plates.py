from plates import is_valid

def test_one():
    assert is_valid("AA7U") == False

def test_two():
    assert is_valid("AA77") == True

def test_three():
    assert is_valid("A87") == False

def test_four():
    assert is_valid("AA79") == True

def test_five():
    assert is_valid("HI!44") == False

def test_six():
    assert is_valid("RUSH1108") == False

def test_seven():
    assert is_valid("RD1108") == True

def test_eight():
    assert is_valid("AR096") == False
