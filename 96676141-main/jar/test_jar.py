from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar_custom_capacity = Jar(20)
    assert jar_custom_capacity.capacity == 20
    assert jar_custom_capacity.size == 0

    with pytest.raises(ValueError):
        jar = Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(20)
    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)

    jar.withdraw(3)
    assert jar.size == 2

    try:
        jar.withdraw(5)
    except ValueError:
        pass
    else:
        assert False
