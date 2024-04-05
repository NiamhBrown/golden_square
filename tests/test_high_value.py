from lib.high_value import *

def test_first_value_is_higher():
    high_value = HighValue(7,2)
    results = high_value.get_highest()
    assert results == "First value is higher"

def test_second_value_is_higher():
    high_value = HighValue(2,7)
    results = high_value.get_highest()
    assert results == "Second value is higher"

def test_values_are_equal():
    high_value = HighValue(7,7)
    results = high_value.get_highest()
    assert results == "Values are equal"