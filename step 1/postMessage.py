#
#Post messages to a room given roomid
#

import requests
import json

def postMessage(message,roomid):
    url = "https://api.ciscospark.com/v1/messages"
    payload = {
        'roomId': roomid,
        'text': message
    }
    header = {'Content-type': 'application/json; charset=utf-8',
              'Authorization': 'Bearer ODUxOGFiMDctMWIwZS00MGY1LWJmNzctMGUzMmY5NjE5MjY5ZWQzM2I0OGItOWVm'}

    response = requests.post(url, headers=header, data=json.dumps(payload))
    # print r.json()
    if response.status_code == 200:
        return 'Success'
    else:
        return 'Failed'