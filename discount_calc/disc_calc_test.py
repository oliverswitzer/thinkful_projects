
import unittest
from disc_calc import DiscountCalculator

class DiscountCalculatorTests(unittest.TestCase):
	def test_ten_percent_discount(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(100,10,'percent')
		self.assertEqual(10.0, result)

	def fifteen_percent_discount_test(self):
	    discount_calculator = DiscountCalculator()
	    result = discount_calculator.calculate(100,15,'percent')
	    self.assertEqual(15.0, result)

	def absolute_discount_test(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(250, 5, 'absolute')
		self.assertEqual(5, result)

	def discount_type_test(self):
		discount_calculator = DiscountCalculator()
		self.assertRaises(ValueError, discount_calculator.calculate, 250, 5, 'random')

	def float_value_test_for_percentage_discount(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(100.0, 10.0, 'percent')
		self.assertEqual(10.0, result)

	def float_value_test_for_absolute_discount(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(100.0, 10.0, 'absolute')
		self.assertEqual(10.0, result)

	def excessive_percentage_discount_amount_test(self):
		discount_calculator = DiscountCalculator()
		self.assertRaises(ValueError, discount_calculator.calculate, 250, 110, 'percent')

	def excessive_absolute_discount_amount_test(self):
		discount_calculator = DiscountCalculator()
		self.assertRaises(ValueError, discount_calculator.calculate, 100, 125, 'absolute')





