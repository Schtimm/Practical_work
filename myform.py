from xmlrpc.client import DateTime
from bottle import post, request
from datetime import datetime
import re
import pdb
import json
@post('/home', method='post')
def my_form():
    pattern=r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
    mail = request.forms.get('ADRESS')
    login=request.forms.get('Username')
    question=request.forms.get('QUEST')
    #pdb.set_trace()
    data={}
    if(mail!="" and login!="" and question!=""):
        if(re.match(pattern, mail) is not None):
            #data[mail]=question
            data[mail]=[login, question]
            with open('data.txt') as json_file:
                    content = json_file.read()
                    if(content!=""):
                        content=json.loads(content)
                        if mail not in content:
                            json_file.close()
                            with open('data.txt', 'a') as outfile:
                                if(len(question)>3 and question.isdigit()==False):
                                    json.dump(data, outfile)
                                else:
                                    return "The question must be longer then 3 symbols and not consist of only digits.\
                                    access date: "+str(datetime.now().date())
                        else:
                            json_file.close()
                            with open('data.txt') as json_file:
                                data=json.load(json_file)
                                if(question not in data[mail]):
                                    data[mail].append(question)
                                json_file.close()
                                with open('data.txt', 'w') as json_file:
                                    if(len(question)>3 and question.isdigit()==False):
                                        json.dump(data, json_file)
                                    else:
                                        return "The question must be longer then 3 symbols and not consist of only digits.\
                                        access date: "+str(datetime.now().date())
                    else:
                        with open('data.txt', 'a') as outfile:
                            if(len(question)>3 and question.isdigit()==False):
                                json.dump(data, outfile)
                            else:
                                return "The question must be longer then 3 symbols and not consist of only digits.\
                                access date: "+str(datetime.now().date())
            return "Thanks, " +str(login)+"! The answer will be sent to the mail %s" % mail+"\
            access date: "+str(datetime.now().date())
        else:
            return "Sorry! The Email %s" % mail+" is incorrect.\
            access date: "+str(datetime.now().date())
    if(mail=="" and login!="" and question!=""):
        return "Fill the Email adress field please\
        access date: "+str(datetime.now().date())
    if(mail!="" and login=="" and question!=""):
        if(re.match(pattern, mail) is None):
            return "Fill the login field please\
            The Email %s" % mail+" is incorrect.\
            access date: "+str(datetime.now().date())
        else:
            return "Fill the login field please\
            access date: "+str(datetime.now().date())
    if(mail=="" and login=="" and question!=""):
        return "Fill the login and Email adress fields please\
        access date: "+str(datetime.now().date())
    if(mail=="" and login=="" and question==""):
        return "Fill the login and Email adress fields please, also write your question\
        or we will be unable to answer\
        access date: "+str(datetime.now().date())
    if(mail!="" and login!="" and question==""):
        if(re.match(pattern, mail) is None):
            return "write your question or we will be unable to answer\
            The Email %s" % mail+" is incorrect.\
            access date: "+str(datetime.now().date())
        else:
            return "write your question or we will be unable to answer\
            access date: "+str(datetime.now().date())
    if(mail=="" and login!="" and question==""):
        return "Fill the Email adress field please and write your question or we will be unable to answer\
        access date: "+str(datetime.now().date())
    if(mail!="" and login=="" and question==""):
        if(re.match(pattern, mail) is None):
            return "Fill the login field please\
            and write your question or we will be unable to answer\
            The Email %s" % mail+" is incorrect.\
            access date: "+str(datetime.now().date())
        else:
            return "Fill the login field please\
            and write your question or we will be unable to answer\
            access date: "+str(datetime.now().date())

