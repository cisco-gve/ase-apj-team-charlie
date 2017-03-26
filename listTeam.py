#
#To retrieve the list of Teams' names
#

import requests
import json

def listTeam():
    url = "https://api.ciscospark.com/v1/teams"
    header = {'Content-type': 'application/json; charset=utf-8',
              'Authorization': 'Bearer ODUxOGFiMDctMWIwZS00MGY1LWJmNzctMGUzMmY5NjE5MjY5ZWQzM2I0OGItOWVm'}
    response = requests.get(url, headers=header)
    a = response.json()
    b = a['items']
    c = []
    for room in b:
        c.append(room['name'])
    return c

print listTeam()
