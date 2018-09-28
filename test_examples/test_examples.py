# content of test_sample.py
def increment(x):
    return x + 1


def test_increment_3_by_1_is_4():
    assert increment(3) == 4

def test_increment_minus_3_by_1_is_minus_2():
    assert increment(-3) == -2

def test_increment_minus_1_by_1_is_0():
	assert increment(-1) == 0

def test_set_comparison():
    set1 = set("1308")
    set2 = set("3018")
    assert set1 == set2

def test_set_comparison():
    set1 = set("1234")
    assert set1 == {'2', '4', '1', '3'}

