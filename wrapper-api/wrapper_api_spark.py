import json
import sys
import requests

ACCESS_TOKEN = "OTU1MzA5OTktNGFjNC00YjI5LWJhNWItNGM2MTExYWViYzQ1NWI2YzIwZGItOWM4"
'''BOT_ACCESS_TOKEN = "Y2ZjMDRjOTgtZGU0ZC00N2FkLWJkODEtN2JmNzY5MzQzNmU5ODA4OTM0YjYtZDRk"'''
ROOM_NAME = "Room_test"
YOUR_MESSAGE = "test" 

#sets the header to be used for authentication and data format to be sent.
def setHeaders():
	accessToken_hdr = 'Bearer ' + ACCESS_TOKEN
	spark_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
	return (spark_header)

#sets the BOT haeder
#def setBOTHeaders():

	

# creates a new room and returns the room id.
def createRoom(the_header,room_name):
	roomInfo = '{"title":"' + room_name + '"}'
	uri = 'https://api.ciscospark.com/v1/rooms'
	resp = requests.post(uri, data=roomInfo, headers=the_header)
	var = resp.json()
	print("createRoom JSON: ", var)
	return var ["id"]

#posts a message to the room
def postMsg(the_header,roomId,message):
	message = {"roomId":roomId,"text":message}
	uri = 'https://api.ciscospark.com/v1/messages'
	resp = requests.post(uri, json=message, headers=the_header)
	print("postMsg JSON: ", resp.json())

#get room details
def getRoomInfo(the_header,roomId):
	print("In function getRoomInfo")
	uri = None
	if uri == None:
		sys.exit("Please add the uri call to get room details.  See the Spark API Ref Guide")
	resp = requests.get(uri, headers=the_header)
	print("getRoomInfo JSON", resp.json())

#Bot integration
#def Bot()

'''if __name__ == '__main__':
	if ACCESS_TOKEN==None or ROOM_NAME==None or YOUR_MESSAGE==None:
		sys.exit("Please check that variables ACCESS_TOKEN, ROOM_NAME and YOUR_MESSAGE have values assigned.")
	header=setHeaders()
	room_id=createRoom(header,ROOM_NAME)
	postMsg(header,room_id,YOUR_MESSAGE)
'''