
#Sending SMS messages with script API

call("+14155550000", {
   "network":"SMS"})
say("Don't forget your meeting at 2 p.m. on Wednesday!")



#Sending SMS messages with Web API

from itty import *
from tropo import Tropo, Session

@post('/index.json')
def index(request):

	t = Tropo()
	t.call(to="+14075550100", network = "SMS")
	t.say("Tag, you're it!")
	
	return t.RenderJson()

run_itty(server='wsgiref', host='0.0.0.0', port=8888)

