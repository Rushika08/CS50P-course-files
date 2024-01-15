from numb3rs import validate

def test_validate_true():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("55.56.89.76") == True
    assert validate("203.255.224.200") == True
    assert validate("156.199.100.123") == True
    assert validate("1.0.2.9") == True
    assert validate("025.045.009.000") == True

def test_validate_false():
    assert validate("270.255.255.255") == False
    assert validate("255.400.0.65") == False
    assert validate("98.255.1000.") == False
    assert validate("255.255.2.01999") == False
    assert validate("255.255.255") == False
    assert validate("255.255.67.255.255") == False

