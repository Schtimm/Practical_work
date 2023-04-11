from xmlrpc.client import DateTime
from bottle import post, request
from datetime import datetime
@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    login=request.forms.get('Username')
    question=request.forms.get('QUEST')
    if(mail!="" and login!="" and question!=""):
        if(mail.find("@", 0, len(mail)-1)!=-1 and mail.find(".", 0, len(mail)-1)!=-1):
            return "Thanks, " +str(login)+"! The answer will be sent to the mail %s" % mail+"\
            access date: "+str(datetime.now().date())
        else:
            return "Sorry! The Email %s" % mail+" is incorrect.\
            access date: "+str(datetime.now().date())
    if(mail=="" and login!="" and question!=""):
        return "Fill the Email adress field please\
        access date: "+str(datetime.now().date())
    if(mail!="" and login=="" and question!=""):
        if(mail.find("@", 0, len(mail)-1)==-1 or mail.find(".", 0, len(mail)-1)==-1):
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
        if(mail.find("@", 0, len(mail)-1)==-1 or mail.find(".", 0, len(mail)-1)==-1):
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
        if(mail.find("@", 0, len(mail)-1)==-1 or mail.find(".", 0, len(mail)-1)==-1):
            return "Fill the login field please\
            and write your question or we will be unable to answer\
            The Email %s" % mail+" is incorrect.\
            access date: "+str(datetime.now().date())
        else:
            return "Fill the login field please\
            and write your question or we will be unable to answer\
            access date: "+str(datetime.now().date())

