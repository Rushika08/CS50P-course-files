from um import count

def test_one():
    assert count("UM um Um uM") == 4
    assert count("..Um.. hello") == 1

def test_two():
    assert count("UmUm") == 0
    assert count("Yummy") == 0
    assert count("mum is um") == 1

def test_three():
    assert count("um..um.. Yummy") == 2
