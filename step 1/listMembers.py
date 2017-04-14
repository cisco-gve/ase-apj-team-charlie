#
#To retrieve the list of room members
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

def listMembers():
    url = "https://api.ciscospark.com/v1/memberships"
    header = {'Content-type': 'application/json; charset=utf-8',
              'Authorization': 'Bearer' + token}
    r = requests.get(url, headers=header)
    a = r.json()
    b = a['items']
    c = []
    for people in b:
        c.append(people['personEmail'])
    return c

print listMembers()