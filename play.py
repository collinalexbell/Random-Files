import serial
import time
import socket
TCP_IP='localhost'
TCP_PORT = 3007

sock = socket.socket(socket.AF_INET,
							socket.SOCK_STREAM)
#sock.connect((TCP_IP, TCP_PORT));
#buffer = 1024


ser = serial.Serial("/dev/ttyACM0")
ser.baudrate = 9600

def stop():
	ser.write('4')
	time.sleep(.5)

def forward():
	ser.write(('3'))

def backward():
	ser.write('2')

def left():
	ser.write('3')
	time.sleep(.2)
	ser.write('0')

def backLeft():
	ser.write('2')
	time.sleep(.2)
	ser.write('0')


def right():
	ser.write('3')	
        time.sleep(.2)
        ser.write('1')

def backRight():
	ser.write('2')
	time.sleep(.2)
	ser.write('1')	
	time.sleep(.4)
	ser.write('4')

def fire():
	ser.write('7')

def rreload():
	ser.write('8')

if (__name__ == "__main__"):
        while(True):
            forward()
            time.sleep(.2)
            right()
            time.sleep(1)
            backward()
            time.sleep(.2)
            backRight()
            time.sleep(1)
            forward()
            time.sleep(.2)
            right()
            time.sleep(1)
            backward()
            time.sleep(.2)
            backRight()
            time.sleep(1)
            stop()
            forward()
            time.sleep(.2)
            left()
            time.sleep(1)
            backward()
            time.sleep(.2)
            backLeft()
            time.sleep(1)
            forward()
            time.sleep(.2)
            left()
            time.sleep(1)
            backward()
            time.sleep(.2)
            backLeft()
            time.sleep(1)
            stop()
            time.sleep(6)
            forward()
            time.sleep(1)
	

else:
    while True:
            i = input()
            if (i!=None):
                print (i)
            if (i == "w"):
                forward()
            if (i == "s"):
                backward()
            if (i == "a"):
                left()
            if (i == "d"):
                right()
            if (i == "e"):
                stop()
            if (i == "z"):
                backLeft()
            if (i == "c"):
                backRight()
            if (i == "f"):
                fire()
            if (i == "r"):
                rreload()

