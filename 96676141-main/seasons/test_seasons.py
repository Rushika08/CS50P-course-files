from seasons import convert
from datetime import date

def test_one():
    reference_date = date(2023, 12, 14)
    assert convert("2022-12-14", reference_date) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert("2021-12-14", reference_date) == "One million, fifty-one thousand, two hundred minutes"
