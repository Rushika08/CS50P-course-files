from twttr import shorten

def test_shorten_lower():
    assert shorten("Rushika") == "Rshk"

def test_shorten_upper():
    assert shorten("DAVID") == "DVD"

def test_shorten_numbers():
    assert shorten("rushi1108") == "rsh1108"

def test_shorten_punctuation():
    assert shorten("Hi! Jaya..") == "H! Jy.."
