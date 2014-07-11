import serial
import time
import socket
import voice

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

        

from SimpleCV import Image
from SimpleCV import Color
import time


def segment(img, w_segments, h_segments, show = False):
    img_w, img_h = img.size()
    section_w = img_w/w_segments
    section_h = img_h/h_segments
    segments = []
    for i in range(w_segments):
        segments.append([])
        for j in range(h_segments):
            segments[i].append(img.crop(i*section_w, j*section_h, section_w, section_h))

    if (show == True):
        for i in segments:
            for j in i:
                j.show()
                time.sleep(3)

    return segments

def assign_number(segments):
    white_segments = []
    for i in segments:
        white_segments.append([])
        for j in i:
            white_pic = j.hueDistance(Color.GRAY)
            white_pic = white_pic - j
            mean_color = white_pic.meanColor()
            #print(mean_color)
            if (mean_color[1] > 2 and mean_color[2] > 2):
                white_segments[-1].append(True)
            else:
                white_segments[-1].append(False)
    print(white_segments)
    if (white_segments[0][0] is True and white_segments[0][1] is True):
        return "LEFT"
    if (white_segments[1][0] is True and white_segments[1][1] is True):
        return "CENTER"
    if (white_segments[2][0] is True and white_segments[2][1] is True):
        return "RIGHT"
    else:
        return "NONE"
            



from SimpleCV import Camera
import time
import math

cam = Camera()

def run_camera(seconds):
    start_time = time.time()
    while True:
        if(time.time()-start_time > seconds):
            break
        print(math.floor(time.time()-start_time))
        img = cam.getImage()
        img = img.lowPassFilter()
        img.show()

def take_picture():
    run_camera(3)
    img = cam.getImage()
    return img

if (__name__ == "__main__"):
    while(True):
        pic = take_picture()
        segs = segment(pic, 3, 2)
        direction = assign_number(segs)
        if direction is "LEFT":
            left()
        if direction is "RIGHT":
            right()
        if direction is "CENTER":
            forward()
        time.sleep(.2)
        stop()
