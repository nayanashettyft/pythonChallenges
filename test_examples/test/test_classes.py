import unittest
from app.greaterthan import Greaterthan

class TestGreaterthan(unittest.TestCase):
	
	def test_11_is_greater_than_10():
		obj = Greaterthan()
		self.assertEqual(obj.isgreaterthan10(11), True)

