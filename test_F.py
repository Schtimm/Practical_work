import unittest
import re
pattern=r"[a-zA-Z0-9._&='\-+]{1,256}@[a-zA-Z0-9]{1,100}\.[a-zA-Z0-9]{1,7}"
def checkmail(mail):
    if(re.match(pattern, mail) is not None and mail.count("@")==1 and mail.split("@")[0].isdigit==False):
        return True
    else:
        return False
incorrectemails=["gmail.com", "so.mething@gmail..com", "in.cor@gmailcom", "incor@gmail.c", "", "m1@",
                 "11111111@gmail.com", "mail", ".", "ma il@gmail.com", "mail()<>[]@gmail.com",
                 "m"]
class Test_test_F_mail(unittest.TestCase):
    def test_A(self):
        for i in range(len(incorrectemails)):
            self.assertFalse(checkmail(incorrectemails[i]), incorrectemails[i]+" is correct")

if __name__ == '__main__':
    unittest.main()
