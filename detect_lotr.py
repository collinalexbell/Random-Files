
from SimpleCV import ROI
from SimpleCV import Camera
from SimpleCV import TemporalColorTracker
from SimpleCV import Display
from SimpleCV import Color

while(True):
    cam = Camera()
    img = cam.getImage()
    feat = img.findBlobs()
    feat[-3].show()
