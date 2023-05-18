import re
def checkphone(phone):
    pattern=r"\+\d+-\(\d{3}\)-\d{3}-\d{2}-\d{2}"
    if(re.match(pattern, phone) is not None):
        return True
    else:
        return False
def checklogin(login):
    if(len(login)>3 and login.isdigit!=True):
        return True
    else:
        return False
def checkreview(review):
    if(len(review)>3 and review.isdigit!=True):
        return True
    else:
        return False
