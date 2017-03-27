
#Basic Menu with Transfer with Script API

say("Welcome to the Tropo company directory. Who are you trying to reach? ")
result = ask("Press 1 for Jason, 2 for Adam and 3 for Jose ", {
   "choices":"1, 2, 3",
   "attempts":3,
   "mode":"dtmf"
    })

if (result.value == "1"):
   say("Connecting you to Jason")
   transfer("+14155550100")
elif (result.value == "2"):
   say("Connecting you to Adam")
   transfer("+19165550100")
elif (result.value == "3"):
   say("Connecting you to Jose")
   transfer("+14075550100")



#Basic Menu with Transfer with Web API  

from itty import *
from tropo import Tropo, Session

@post('/index.json')
def index(request):

	s = Session(request.body)
	callerID = s.fromaddress['id']
	t = Tropo()

	if(callerID == '4075550100') :
		t.say("Sending you to Adam.")
		t.transfer("+611300975708")
	elif (callerID == '3865550100') :
		t.say("Sending you to Jason.")
		t.transfer("")
	else :
		t.say("You get nothing!")
		
	return t.RenderJson()

run_itty(server='wsgiref', host='0.0.0.0', port=8888)


    


