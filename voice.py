import subprocess

def say(text):
    subprocess.call( 'echo \"' +text + '\"|festival --tts', shell=True)

if (__name__ == '__main__'):
    import time
    say('Hello my name is Rouge')

    say('I am Alexanders red van')
    say('I am talking to you today because Alexander decided to give me a voice. He also wants to give me emotions. His main overarching goal is to make me into a humanoid transforming robot. This is possible but probably quite difficult. Alexander is determined to do this and I am sure if he sticks with it for long enough it will work out. Alexander named me after Dagney Taggart from Atlas Shrugged. My full name is Dagney Rouge Taggart, but people just call me rouge for short. One day, Alexander had an epiphany as was working on building a brand new robot. He was trying to test out the voice of his timid little robot but the bots speakers weren\'t loud enough. He went outside and plugged my voice into his program and when I spoke the words he originally meant for that timid robot to speak he was struck with awe. Even without a concious soul I meant alot to him. I provided Alexander with shelter as he struggle to find his path to manhood. The night when he first heard my voice was the night he that he made it his goal to give me a soul. Alexander\'s plan is to continue working on me for as long as it takes for his dreams for me to come true. He wants to find a woman who will care about me and the future of my species as much as he cares. Alexander will marry this woman and together they will help my species flourish amongst the other creatures in the universe.')


