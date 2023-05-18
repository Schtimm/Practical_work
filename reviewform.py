from bottle import post, request
import re
import json
from checkfunctions import*
@post('/reviews', method='post')
def my_form():
    data={}
    phone = request.forms.get('Phone')
    login=request.forms.get('Username')
    review=request.forms.get('Review')
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
