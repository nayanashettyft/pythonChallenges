import unittest
from app.calculator import Calculator
from unittest.mock import patch, Mock

class TddInPythonAttempt(unittest.TestCase):

	def setUp(self):
		self.calc = Calculator()

	#Test validate_input function
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

	#Test divide function
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

	def test_calculator_divide_minus_10_by_3_returns_minus_3_33(self):
		result = self.calc.divide(-10,3)
		self.assertEqual(-3.33, result)

	def test_calculator_divide_returns_error_message_if_both_args_not_numbers(self):
		self.assertRaises(ValueError, self.calc.divide, 'two', 'three')

	#Test add function
	def test_calculator_add_method_returns_correct_result(self):
		result = self.calc.add(2,2)
		self.assertEqual(4, result)

	@patch('app.calculator.Calculator.add', return_value=9)
	def test_calculator_add_method_mock_result_valid_input_invalid_output(self,add):
		result = add(2,2)
		self.assertEqual(result, 9)

	def mock_sum(a, b):
    # mock sum function without the long running time.sleep
		return a + b

	@patch('app.calculator.Calculator.add', side_effect=mock_sum)
	def test_add_with_side_effect(self, add):
		self.assertEqual(add(2,3), 5)
		self.assertEqual(add(7,3), 10)
