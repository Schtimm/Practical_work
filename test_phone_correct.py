import unittest
import re
from checkfunctions import*
correctphones=["+7-(981)-122-33-25", "+8-(900)-245-11-83", 
               "+43-(917)-150-25-74", "+375-(925)-118-45-14",
               "+43-(911)-678-29-11", "+7-(912)-311-28-09", "+55-(909)-115-38-75", 
               "+30-(901)-217-63-81", "+7-(900)-134-37-15",
               "+375-(902)-781-37-43", "+33-(907)-118-31-79"]
class Test_test_phone_correct(unittest.TestCase):
    def test_A(self):
        for i in range(len(correctphones)):
            self.assertTrue(checkphone(correctphones[i]), correctphones[i]+" is incorrect")

if __name__ == '__main__':
    unittest.main()
