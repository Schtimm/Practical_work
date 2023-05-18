import unittest
import re
pattern=r"[a-zA-Z0-9._&='\-+]{1,256}@[a-zA-Z0-9]{1,100}\.[a-zA-Z0-9]{1,7}"
def checkmail(mail):
    if(re.match(pattern, mail) is not None and mail.count("@")==1):
        return True
    else:
        return False
correctemails=["johnsmith@gmail.com", "Johnsmith@gmail.com", "NEWMAIL@gmail.com", "something@rambler.ru",
               "m.m@mail.ru", "m1@gmail.com", "login@domen.ru", "alice+test@example.com", "user123@gmail.com",
               "support@example.org", "john.doe@gmail.com"]
class Test_test_T_mail(unittest.TestCase):
    def test_A(self):
        for i in range(len(correctemails)):
            self.assertTrue(checkmail(correctemails[i]), correctemails[i]+" is incorrect")

if __name__ == '__main__':
    unittest.main()
