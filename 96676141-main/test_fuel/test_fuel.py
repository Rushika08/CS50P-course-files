from fuel import convert, gauge
import pytest

def test_one():
    assert convert("99/100") == 99
    assert convert("87/99") == 88

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("87/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("95/85")

def test_two():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(87) == "87%"
