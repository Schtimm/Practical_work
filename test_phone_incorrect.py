import unittest
import re
from checkfunctions import*
incorrectphones=["+7--122-33-25", "+8-(90)-245-11-83", 
               "+43-(917)-15-25-74", "+375-(925)-118",
               "+(911)-678-29-11", "+7", "+55-(909)-38-75", 
               "+30-(901)-(217)-63-81", "+7-(900)-abc-37-15",
               "+375-(902)-781-1-43", ""]
class Test_test_phone_incorrect(unittest.TestCase):
    def test_A(self):
        for i in range(len(incorrectphones)):
            self.assertFalse(checkphone(incorrectphones[i]), incorrectphones[i]+" is correct")

if __name__ == '__main__':
    unittest.main()
