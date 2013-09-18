
import unittest
from calculator import Calculator
 
class TddInPythonExample(unittest.TestCase):
 
	def test_calculator_add_method_returns_correct_result(self):
      self.calc.add(2,2)
      result = calc.add(2,2)
      self.assertEqual(4, result) 

	
	def setUp(self):
		self.calc = Calculator()