#
#To retrieve the list of room members
#

import requests
import json

def listMembers():
    url = "https://api.ciscospark.com/v1/memberships"
    header = {'Content-type': 'application/json; charset=utf-8',
              'Authorization': 'Bearer ODUxOGFiMDctMWIwZS00MGY1LWJmNzctMGUzMmY5NjE5MjY5ZWQzM2I0OGItOWVm'}
    r = requests.get(url, headers=header)
    a = r.json()
    b = a['items']
    c = []
    for people in b:
        c.append(people['personEmail'])
    return c

print listMembers()