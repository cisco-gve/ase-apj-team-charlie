
#Asking Questions and Digits Exmaple

ask("What's your favorite color?", {
    "choices":"red, blue, green",
    "timeout":10.0,
    "attempts":3,
    "onChoice": lambda event : say("You chose " + event.value),
    "onBadChoice": lambda event : say("I'm sorry,  I didn't understand that. You can select red, blue, or green.")
})



#Asking for Digits

result = ask("Pick a number from 0 to 9", {
     "choices":"[1 DIGIT]"})

say("You said " + result.value)
log("They said " + result.value)



#Asking Questions and Digits Exmaple with Web API

from itty import *
from tropo import Tropo, Result

@post('/index.json')
def index(request):

	t = Tropo()
	t.ask(choices = "red, blue, green", timeout=60, name="color", say = "What's your favorite color?  Choose from red, blue or green.")		
	t.on(event = "continue", next ="/continue")
	return t.RenderJson()
	
@post("/continue")
def index(request):
	
	r = Result(request.body)
	t = Tropo()	
	answer = r.getValue()	
	t.say("You said " + answer)	
	return t.RenderJson()
	
run_itty(server='wsgiref', host='0.0.0.0', port=8888)

