import unittest
from lib.Validator import ValidationProcessing

class ValidationProcessingSpec(unittest.TestCase):

    def test_ValidationProcessing_postive_number_returns_true(self):
        vp = ValidationProcessing({'number': 2})
        #assert vp.is_positive() == True
        self.assertEqual(vp.is_positive(), True)