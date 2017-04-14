#
#To retrieve the list of rooms' titles
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

def listRoom():
    url ="https://api.ciscospark.com/v1/rooms"
    header = {'Content-type':'application/json; charset=utf-8',
              'Authorization': 'Bearer' + token}
    response = requests.get(url, headers = header)
    a = response.json()
    b = a['items']
    c = []
    for room in b:
        c.append(room['title'])
    return c

print listRoom()