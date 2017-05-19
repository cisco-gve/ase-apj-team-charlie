#
#Add a new member to the room, input the person email
#

import requests
import json

def load_settings(settingsFile):
    """Reads settings file into an list.
    :param settingsFile: the name of the settings file e.g. ``'settings.txt'``
    :type settingsFile: string
    :returns: the newly-created list
    """

    with open(settingsFile, 'r') as fileHandle:
        settings = fileHandle.readlines()
    fileHandle.close()

    return settings

# Loading the settings
app_settings = load_settings("setting.txt")
token = app_settings[0].rstrip()

def addMember(personEmail):
    url = 'https://api.ciscospark.com/v1/memberships'
    header = {'Content-type': 'application/json; charset=utf-8',
              'Authorization': 'Bearer ' + token}
    payload = {'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vMGU0MGRhMjAtMGQ1Mi0xMWU3LTg0ODAtYzcyN2M5YzlmYzA2',
               'personEmail': 'r2d2@example.com',
               }
    response = requests.post(url, headers=header, data=json.dumps(payload))
    #print r.json()
    if response.status_code == 200:
        return 'Add {} Succeed'.format(personEmail)
    else:
        return 'Add Member Failed'