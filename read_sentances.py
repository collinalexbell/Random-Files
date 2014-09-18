import voice 

with open ("documents/sentance_a_day.txt", "r") as myfile:
        data=myfile.read().replace('\n', '')

voice.say(data)
