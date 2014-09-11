from driver import driver
import random
import time
import pyttsx
import voice

robot = driver(True)
go = True

def start_workout(min=5, max=10):
    number = random.randint(min, max)
    print(number)
    voice.say("You are going to do " + str(number) + " pushups")
    time.sleep(.5)
    voice.say("Three")
    time.sleep(1.9)
    voice.say("Two")
    time.sleep(1.9)
    voice.say("One")
    time.sleep(1.9)
    voice.say("Go!")

    
    #print("This is your robot coach. Lets do some pushups")
    #min = int(raw_input("Enter the minimum amount of pushups you are willing to do\n"))
    #max = int(raw_input("Enter the maximum amount of pushups you are willing to do\n"))
    for i in range(number):
            robot.forward()
            time.sleep(.4)
            robot.stop()
            robot.backward()
            time.sleep(.5)
            robot.stop()
            time.sleep(1)
            voice.say(str(i+1))

if (__name__ == "__main__"):
    start_workout()
