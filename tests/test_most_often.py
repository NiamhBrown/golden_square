from lib.most_often import *

def test_new_item_added():
    most_often = MostOften([])
    most_often.add_new("tooth paste")
    result = most_often.starting_list
    assert result == ["tooth paste"]

def test_multiple_items_added():
    most_often = MostOften([])
    most_often.add_new("tooth paste")
    most_often.add_new("tooth brush")
    most_often.add_new("floss")
    result = most_often.starting_list
    assert result == ["tooth paste", "tooth brush", "floss"]

def test_unique_items():
    most_often = MostOften([])
    most_often.add_new("tooth paste")
    most_often.add_new("tooth paste")
    most_often.add_new("tooth paste")
    most_often.add_new("tooth brush")
    most_often.add_new("tooth brush")
    most_often.add_new("floss")
    most_often.calculate_unique_list()
    result = most_often.unique_items
    assert result == ["tooth paste", "tooth brush", "floss"]


