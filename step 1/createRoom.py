#
#Create a new room, input the room title
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
app_settings = load_settings("settings.txt")
token = app_settings[0].rstrip()

def createRoom(roomTitle):
    url = "https://api.ciscospark.com/v1/rooms"
    header = {'Content-type': 'application/json',
              'Authorization': 'Bearer' + token}
    payload = {'title': roomTitle}
    response = requests.post(url, headers=header,data=json.dumps(payload))
    # print r.json()
    if response.status_code == 200:
        return 'Create Room {} Succeed'.format(roomTitle)
    else:
        return 'Create Room Failed'

