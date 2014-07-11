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
        img.show()

print("Position camera with line in the center")
run_camera(15)
img = cam.getImage()
img.save('line_center.jpg')

print("Position camera with line to left of robot")
run_camera(15)
img = cam.getImage()
img.save('line_left.jpg')

print("Position camera with line to right of robot")
run_camera(15)
img = cam.getImage()
img.save('line_right.jpg')


