from SimpleCV import Camera

camera = Camera()

while True:
    img = camera.getImage()
    x,y = img.size()
    section = x/3
    right = img.crop(0,y/4,x/3, (3*y)/4)
    left = img.crop((2*x)/3,y/4,x,(3*y/4))
    left.show()

