#!/bin/python


import time
import webbrowser
import random, os


file_path = ""
if os.path.isfile(file_path) == False:
        print "ERROR: file not present"


print "What time do you want to wake up?"

print "Use this form.\nExample: 06:30"

Alarm = input()


Time = time.strftime("%H:%M")

with open("YT.txt") as f:
    content = f.readlines()


while Time != Alarm:

    print "The time is" + Time

    Time = time.strftime("%H:%M")
    time.sleep(6)


if Time == Alarm:

    print "Time to Wake up"

    #random_video = random.choice(content)
#webbrowser.open("https://www.youtube.com/watch?v=hT_nvWreIhg")

