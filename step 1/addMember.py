#
#Add a new member to the room, input the person email
#

import requests
import json


def addMember(personEmail):
    url = 'https://api.ciscospark.com/v1/memberships'
    header = {'Content-type': 'application/json; charset=utf-8',
              'Authorization': 'Bearer ODUxOGFiMDctMWIwZS00MGY1LWJmNzctMGUzMmY5NjE5MjY5ZWQzM2I0OGItOWVm'}
    payload = {'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vMGU0MGRhMjAtMGQ1Mi0xMWU3LTg0ODAtYzcyN2M5YzlmYzA2',
               'personEmail': 'r2d2@example.com',
               }
    response = requests.post(url, headers=header, data=json.dumps(payload))
    #print r.json()
    if response.status_code == 200:
        return 'Add {} Succeed'.format(personEmail)
    else:
        return 'Add Member Failed'