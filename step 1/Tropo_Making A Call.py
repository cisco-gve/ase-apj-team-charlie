
#Miking a Call 

call("+14155550100", {
   "timeout":120,
   "onAnswer": lambda event : say("Hello,this is Charlie from Beijing!") and log("Obnoxious call complete"),
   "onTimeout":lambda event : log("Call timed out"),
   "onCallFailure": lambda event : log("Call could not be completed as dialed")
})




