# content of test_sample.py
def increment(x):
    return x + 1


def test_increment_3_by_1_is_4():
    assert increment(3) == 4

def test_increment_minus_3_by_1_is_minus_2():
    assert increment(-3) == -2

def test_increment_minus_1_by_1_is_0():
	assert increment(-1) == 0