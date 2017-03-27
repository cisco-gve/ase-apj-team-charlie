
#Transferring a Call

say("Transferring you now, please wait.")
transfer("+14075550100")



#Call transferring on SIP/Telephone Network

say("Please wait while we transfer your call. Press star to cancel the transfer.")
transfer(["+14075550100","sip:12345678912@221.122.54.86"], {
    "playvalue":"http://www.phono.com/audio/holdmusic.mp3", 
    "terminator": "*",
    "onTimeout": lambda event : say("Sorry, but nobody answered.")})


#Call transferring Based on callerID

callerID = currentCall.callerID

if (callerID == "4075550100") :
    transfer("+3217105094")
else :
    say("Hi friend!")




#Rejecting a Call Based on callerID

callerID = currentCall.callerID
if (callerID == "4155550100" or callerID == "9165550100") :
    reject()
else :
    say("Hi friend!")


#Transfer and Reject Based on callerID

callerID = currentCall.callerID
if (callerID == "4155550100" or callerID == "9165550100") :
    reject()
elif (callerID == "4075550100") :
    transfer("+13217105094")
else :
    say("Hi friend!")

#Creating a Conference Call

say("Welcome to the hotline!")
conference("THX-1138", {
    "terminator":"*",
    "mute":false,
    "playTones":True})
say("We hope you had fun, call back soon!")






#Transferring a Call with Web API

from itty import *
from tropo import Tropo

@post('/index.json')
def index(request):

	t = Tropo()	
	t.say("Transferring you now, please wait.")
	t.transfer("+14075550100")
	return t.RenderJson()

run_itty(server='wsgiref', host='0.0.0.0', port=8888)


#Transfer and Reject Based on callerID with Web API

from itty import *
from tropo import Tropo, Session

@post('/index.json')
def index(request):

	s = Session(request.body)
	callerID = s.fromaddress['id']
	t = Tropo()
	if(callerID == "4075550100" or callerID == "9165550100") :
		t.reject()
	elif (callerID == '+611300975708') :
		t.transfer("+447700900444")
	else :
		t.say("Hi friend!")		
	return t.RenderJson()

run_itty(server='wsgiref', host='0.0.0.0', port=8888)
    

#Creating a Conference Call with Web API

from itty import *
from tropo import Tropo

@post('/index.json')
def index(request):

	t = Tropo()	
	t.say("Welcome to the conference!")
	t.conference(id = "1234", name = "conference")	
	return t.RenderJson()

run_itty(server='wsgiref', host='0.0.0.0', port=8888)

    


