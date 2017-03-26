
#Answering Incoming Calls

say("Welcome to Tropo! Can I help you?")


#Support Multiple Languages,such as English,French,Korean,Japanese,Italian,Spanish,etc.

say("Hi! This is Kate speaking. Can I help you?", {"voice":"Kate"})


#Playing Audio Files

say("Here's some hold music! https://www.tropo.com/docs/troporocks.mp3")




#Answering Incoming Calls with Web API 

from itty import *
from tropo import Tropo

@post('/index.json')
def index(request):

    t = Tropo()
    t.say("Welcome to Tropo!")
    return t.RenderJson()

run_itty(server='wsgiref', host='0.0.0.0', port=8888)



