
#Transferring a Call

say("Transferring you now, please wait.")
transfer("+14075550100")



#Call transferring on SIP/Telephone Network

say("Please wait while we transfer your call. Press star to cancel the transfer.")
transfer(["+14075550100","sip:12345678912@221.122.54.86"], {
    "playvalue":"http://www.phono.com/audio/holdmusic.mp3", 
    "terminator": "*",
    "onTimeout": lambda event : say("Sorry, but nobody answered.")})


#Call transferring Based on callerID

callerID = currentCall.callerID

if (callerID == "4075550100") :
    transfer("+3217105094")
else :
    say("Hi friend!")




#Rejecting a Call Based on callerID

callerID = currentCall.callerID
if (callerID == "4155550100" or callerID == "9165550100") :
    reject()
else :
    say("Hi friend!")


#Transfer and Reject Based on callerID

callerID = currentCall.callerID
if (callerID == "4155550100" or callerID == "9165550100") :
    reject()
elif (callerID == "4075550100") :
    transfer("+13217105094")
else :
    say("Hi friend!")





    


