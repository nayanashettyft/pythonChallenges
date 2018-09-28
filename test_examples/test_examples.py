# content of test_sample.py
def increment(x):
    return x + 1

def isgreaterthan10(num):
	if num > 10:
		return True
	else:
		return False

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

def test_11_is_greater_than_10():
	assert isgreaterthan10(11) == True

def test_9_is_not_greater_than_10():
	assert isgreaterthan10(9) == False

def test_10_is_not_greater_than_10():
	assert isgreaterthan10(10) == False
