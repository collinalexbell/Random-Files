import subprocess

def say(text):
    subprocess.call( 'echo \"' +text + '\"|festival --tts', shell=True)

if (__name__ == '__main__'):
    import time
    say('Hello my name is Rouge')



