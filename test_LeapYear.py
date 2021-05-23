import unittest
import LeapYear
class TestLeapYear(unittest.TestCase):
    def test_LeapYear_1(self):
        self.assertEqual(LeapYear.leapyear(2012), True)

    def test_LeapYear_2(self):
        self.assertEqual(LeapYear.leapyear(2100), False)

    def test_LeapYear_3(self):
        self.assertEqual(LeapYear.leapyear(2000), True)
    
if __name__=='__main__':
    unittest.main