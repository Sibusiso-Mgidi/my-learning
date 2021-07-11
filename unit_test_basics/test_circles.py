import unittest
import numpy as np
from circles import get_circle_area

class TestCircleArea(unittest.TestCase):
    """
    This is a class consists of test methods. Each method name must start with the name test.
    """
    def test_area(self):
        # Test for area when the radius >= 0
        self.assertAlmostEqual(get_circle_area(1), np.pi)
        self.assertAlmostEqual(get_circle_area(0), 0)
        self.assertAlmostEqual(get_circle_area(2.1), np.pi*np.power(2.1,2))
        

        


