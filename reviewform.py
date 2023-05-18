from bottle import post, request
import re
import json
@post('/reviews', method='post')
def my_form():
    data={}
    phone = request.forms.get('Phone')
    def checkphone(phone):
        pattern=r"\+\d+-\(\d{3}\)-\d{3}-\d{2}-\d{2}"
        if(re.match(pattern, phone) is not None):
            return True
        else:
            return False
    login=request.forms.get('Username')
    def checklogin(login):
        if(len(login)>3 and login.isdigit!=True):
            return True
        else:
            return False
    review=request.forms.get('Review')
    def checkreview(review):
        if(len(review)>3 and review.isdigit!=True):
            return True
        else:
            return False
    if(checklogin(login)!=False and checkreview(review)!=False and checkphone(phone)!=False):
        data[phone]=[login, review]
        with open('reviews.txt') as json_file:
            content = json_file.read()
            if phone not in content:
                json_file.close()
                with open('reviews.txt', 'a') as outfile:
                    json.dump(data, outfile)
            else:
                json_file.close()
                with open('reviews.txt') as json_file:
                    data=json_file.read()
                    data=json.loads(data)
                    if(review not in data[phone]):
                        data[phone][1]=review
                        json_file.close()
                        with open('reviews.txt', 'w') as json_file:
                            json.dump(data, json_file)
        return "Thanks for your review %s, we will contact you in the nearest time"%login
    else:
        return "In order to give a review you must fill all the fields"
