
#Asking Questions and Digits Exmaple

ask("What's your favorite color?", {
    "choices":"red, blue, green",
    "timeout":10.0,
    "attempts":3,
    "onChoice": lambda event : say("You chose " + event.value),
    "onBadChoice": lambda event : say("I'm sorry,  I didn't understand that. You can select red, blue, or green.")
})



#Asking for Digits

result = ask("Pick a number from 0 to 9", {
     "choices":"[1 DIGIT]"})

say("You said " + result.value)
log("They said " + result.value)





