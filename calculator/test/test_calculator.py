import unittest
from app.calculator import Calculator

class TddInPythonAttempt(unittest.TestCase):

	def setUp(self):
		self.calc = Calculator()

	def test_calculator_validate_input_both_ints_is_1(self):
		result = self.calc.validate_input(1,2)
		self.assertEqual(1, result)

	def test_calculator_validate_input_both_floats_is_1(self):
		result = self.calc.validate_input(1.1,2.1)
		self.assertEqual(1, result)

	def test_calculator_validate_input_int_and_float_is_1(self):
		result = self.calc.validate_input(1,2.1)
		self.assertEqual(1, result)

	def test_calculator_validate_input_int_and_complex_is_0(self):
		c = complex(1, 0)
		result = self.calc.validate_input(1,c)
		self.assertEqual(0, result)

	def test_calculator_validate_input_int_and_string_is_0(self):
		result = self.calc.validate_input(1, "four")
		self.assertEqual(0, result)

	def test_calculator_validate_input_negetive_ints_is_1(self):
		result = self.calc.validate_input(-2, -4)
		self.assertEqual(1, result)

	def test_calculator_divide_10_by_5_returns_2(self):
		result = self.calc.divide(10,5)
		self.assertEqual(2, result)

	def test_calculator_divide_5_by_10_returns_half(self):
		result = self.calc.divide(5,10)
		self.assertEqual(0.5, result)

	def test_calculator_divide_10_by_3_returns_3_33(self):
		result = self.calc.divide(10,3)
		self.assertEqual(3.33, result)

	def test_calculator_divide_10_by_3_returns_3_33(self):
		result = self.calc.divide(10,3)
		self.assertEqual(3.33, result)

	def test_calculator_divide_returns_error_message_if_both_args_not_numbers(self):
		self.assertRaises(ValueError, self.calc.divide, 'two', 'three')

	def test_calculator_add_method_returns_correct_result(self):
		result = self.calc.add(2,2)
		self.assertEqual(4, result)