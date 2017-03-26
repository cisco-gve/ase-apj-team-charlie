#
#Create a new room, input the room title
#

import requests
import json


def createRoom(roomTitle):
    url = "https://api.ciscospark.com/v1/rooms"
    header = {'Content-type': 'application/json',
              'Authorization': 'Bearer ODUxOGFiMDctMWIwZS00MGY1LWJmNzctMGUzMmY5NjE5MjY5ZWQzM2I0OGItOWVm'}
    payload = {'title': roomTitle}
    response = requests.post(url, headers=header,data=json.dumps(payload))
    # print r.json()
    if response.status_code == 200:
        return 'Create Room {} Succeed'.format(roomTitle)
    else:
        return 'Create Room Failed'

