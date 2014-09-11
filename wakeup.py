import serial
import voice
import time
import socket
from datetime import datetime
TCP_IP='localhost'
TCP_PORT = 3007

sock = socket.socket(socket.AF_INET,
							socket.SOCK_STREAM)
#sock.connect((TCP_IP, TCP_PORT));
#buffer = 1024


while(True):
    current = datetime.now().hour
    if(current == 3):
        #play()
        voice.say("Wakeup Collin.") 
        voice.say("Its time to build me")


