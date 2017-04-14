#
#Post pictures to a room given roomid
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

def postPicture(picurl ,roomid):
    url = "https://api.ciscospark.com/v1/messages"
    payload={
        'roomId': roomid,
        'file': picurl
    }
    header = {'Content-type': 'application/json; charset=utf-8',
              'Authorization': 'Bearer' + token}

    response = requests.post(url, headers=header,data =json.dumps(payload))
    # print r.json()
    if response.status_code == 200:
        return 'Success'
    else:
        return 'Failed'