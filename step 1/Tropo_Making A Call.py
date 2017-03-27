
#Miking a Call with script API

call("+14155550100", {
   "timeout":120,
   "onAnswer": lambda event : say("Hello,this is Charlie from Beijing!") and log("Obnoxious call complete"),
   "onTimeout":lambda event : log("Call timed out"),
   "onCallFailure": lambda event : log("Call could not be completed as dialed")
})



#Miking a Call with Web API

from itty import *
from tropo import Tropo

@post('/index.json')
def index(request):

	t = Tropo()
	t.call("+14155550100")
	t.say("Tag, you're it!")	
	return t.RenderJson()

run_itty(server='wsgiref', host='0.0.0.0', port=8888)
