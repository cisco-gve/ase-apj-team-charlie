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

def listRoom():
    url = "https://api.ciscospark.com/v1/rooms"
    header = {'Content-type': 'application/json; charset=utf-8',
              'Authorization': 'Bearer ' + token}
    r = requests.get(url, headers=header)
    a = r.json()
    print(a)
    b = a['items']
    c = []
    for room in b:
        c.append(room['title'])
    return c

def listTeam():
    url = "https://api.ciscospark.com/v1/teams"
    header = {'Content-type': 'application/json; charset=utf-8',
              'Authorization': 'Bearer ' + token}
    r = requests.get(url, headers=header)
    a = r.json()
    print(a)
    b = a['items']
    c = []
    for room in b:
        c.append(room['name'])
    return c

def listMembers():
    url = "https://api.ciscospark.com/v1/memberships"
    header = {'Content-type': 'application/json; charset=utf-8',
              'Authorization': 'Bearer ' + token}
    r = requests.get(url, headers=header)
    a = r.json()
    b = a['items']
    c = []
    for people in b:
        c.append(people['personEmail'])
    return c

def createRoom(roomTitle):
    url = "https://api.ciscospark.com/v1/rooms"
    header = {'Content-type': 'application/json',
              'Authorization': 'Bearer ' + token}
    payload = {'title': roomTitle}
    r = requests.post(url, headers=header,data=json.dumps(payload))
    # print r.json()
    if r.status_code == 200:
        return 'Create Room {} Succeed'.format(roomTitle)
    else:
        return 'Create Room Failed'


def addMember(personEmail):
    url = 'https://api.ciscospark.com/v1/memberships'
    header = {'Content-type': 'application/json; charset=utf-8',
              'Authorization': 'Bearer ' + token}
    payload = {'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vMGU0MGRhMjAtMGQ1Mi0xMWU3LTg0ODAtYzcyN2M5YzlmYzA2',
               'personEmail': 'r2d2@example.com',
               }
    r = requests.post(url, headers=header, data=json.dumps(payload))
    #print r.json()
    if r.status_code == 200:
        return 'Add {} Succeed'.format(personEmail)
    else:
        return 'Add Member Failed'

def createTeam(teamName):
    url = "https://api.ciscospark.com/v1/teams"
    header = {'Content-type': 'application/json; charset=utf-8',
              'Authorization': 'Bearer ' + token}
    payload = {'name': teamName}
    r = requests.post(url, headers=header, data=json.dumps(payload))
    # print r.json()
    if r.status_code == 200:
        return 'Create Team {} Succeed'.format(teamName)
    else:
        return 'Create Team Failed'


def listMessage(roomid):
    url = "https://api.ciscospark.com/v1/messages"
    payload = {'roomId': roomid}
    header = {'Content-type': 'application/json; charset=utf-8',
              'Authorization': 'Bearer ' + token}

    r = requests.get(url, headers=header, params=json.dumps(payload))
    a = r.json()
    print(a)


def postMessage(message,roomid):
    url = "https://api.ciscospark.com/v1/messages"
    payload = {
        'roomId': roomid,
        'text': message
    }
    header = {'Content-type': 'application/json; charset=utf-8',
              'Authorization': 'Bearer ' + token}

    r = requests.post(url, headers=header, data=json.dumps(payload))
    # print r.json()
    if r.status_code == 200:
        return 'Success'
    else:
        return 'Failed'

def postPicture(picurl,roomid):
    url = "https://api.ciscospark.com/v1/messages"
    payload={
    'roomId':roomid,
    'file':picurl
    }
    header = {'Content-type': 'application/json; charset=utf-8',
              'Authorization': 'Bearer ' + token}
    
    r = requests.post(url,headers=header,data=json.dumps(payload))
    #print r.json()
    if r.status_code == 200:
        return 'Success'
    else:
        return 'Failed'

'''

if __name__ == '__main__':
    print createTeam('houqin')
    print listTeam()
    print listMembers()
    print createRoom('TEst one')
    print listRoom()
    postPicture('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Youngkitten.JPG/193px-Youngkitten.JPG','Y2lzY29zcGFyazovL3VzL1JPT00vMGU0MGRhMjAtMGQ1Mi0xMWU3LTg0ODAtYzcyN2M5YzlmYzA2')
'''
