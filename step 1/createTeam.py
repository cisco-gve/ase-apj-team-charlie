#
#Create a new team, input the team name
#

import requests
import json

def createTeam(teamName):
    url = "https://api.ciscospark.com/v1/teams"
    header = {'Content-type': 'application/json; charset=utf-8',
              'Authorization': 'Bearer ODUxOGFiMDctMWIwZS00MGY1LWJmNzctMGUzMmY5NjE5MjY5ZWQzM2I0OGItOWVm'}
    payload = {'name': teamName}
    response = requests.post(url, headers=header, data=json.dumps(payload))
    # print r.json()
    if response.status_code == 200:
        return 'Create Team {} Succeed'.format(teamName)
    else:
        return 'Create Team Failed'