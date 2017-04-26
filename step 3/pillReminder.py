from sparkAPI import *
import time

def load_settings(settingsFile):
    """Reads settings file into an list.
    :param settingsFile: the name of the settings file e.g. ``'settings.txt'``
    :type settingsFile: string
    :returns: the newly-created list
    """
    roomDict = {}
    file = open(settingsFile,'r')
    for line in file:
        templist = line.split(':')
        roomDict[templist[0]] = templist[1]

    file.close()
    return roomDict

# Loading the settings
roomDict = load_settings("roomDict.txt")


"""
roomDict = {"TeamA": "Y2lzY29zcGFyazovL3VzL1JPT00vYjE0NzVjZDAtMGVhYi0xMWU3LWFmODEtOGQxMjUyYzJjOTI3",
            "TeamB": "Y2lzY29zcGFyazovL3VzL1JPT00vY2QxYjNiYzAtMGVhYi0xMWU3LWFjNGYtZDdjOWRjYzczNjI3",
            "TeamC": "Y2lzY29zcGFyazovL3VzL1JPT00vZGEyYzZhZjAtMGVhYi0xMWU3LTkyNzktMDM3YmExMzQ3YzRi",
            "TeamD": "Y2lzY29zcGFyazovL3VzL1JPT00vZWM1Nzk1NTAtMWE3OC0xMWU3LWJiZmEtNzM3OGVkMGYxMTk0"}
"""


def pillReminder(timeInterval, mediType, roomID):
    if isinstance(timeInterval, float) is False and isinstance(timeInterval, int) is False:
        print ("Invalid Time Interval")
        return
    if roomID not in roomDict:
        print ("Invalid RoomID")
        return
    for i in range(5):
        time.sleep(timeInterval*2)
        postMessage("Hi patient, time to take %s" % mediType, roomDict[roomID])
        postPicture(picurl, roomDict[roomID])


timeinter = float(input("Please input the time interval(in hour): "))
medicine = input("Please input your medicine: ")
teamname = input("Please input your team name: ")
picurl = 'https://drsvenkatesan.files.wordpress.com/2012/01/aspirin-for-primary-prevention-clopidogrel-meta-analysis.jpg'


pillReminder(timeinter, medicine, teamname)
postPicture(picurl,teamname)


