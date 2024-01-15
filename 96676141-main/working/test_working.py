from working import convert
import pytest

def test_format1_valid():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
    assert convert("12:01 PM to 12:59 AM") == "12:01 to 00:59"
    assert convert("12:01 AM to 1:59 AM") == "00:01 to 13:59"

def test_format1_invalid():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("13:00 PM to 18:00 PM")

def test_format1_valid():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"

def test_format2_invalid():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("5 PM - 9 AM")
    with pytest.raises(ValueError):
        convert("12 AM to 13 PM")
    with pytest.raises(ValueError):
        convert("13 PM to 5 AM")
