import numpy
import math
import pygame
import pygame.camera
from pygame.locals import *


class Line_Bot():
    def __init__(self):
        pass
    def get_orientation(self):
        pass
 
if (__name__ == "__main__"):    
    
    b = (0, 0, 0xFF)
    r = (0xFF, 0, 0)
    g = (0xFF,0xFF , 0xFF)
    t = (125,125, 120)
    
    pygame.init()
    pygame.camera.init()
    size = (640, 480)
    
    d = pygame.display.set_mode(size, 0)
    s = pygame.surface.Surface(size, 0, d)
    c = pygame.camera.list_cameras()
    
    cam = pygame.camera.Camera(c[0], size, "RGB")
    cam.start()
    
    going = True
    prevDir = "none"
    
    s = pygame.surface.Surface(size)
    
    while going:

        if cam.query_image():
            s = cam.get_image(s)
            s2d = pygame.surfarray.array2d(s)
            
            sred = numpy.bitwise_and(s2d, 0xFF0000)
            max = numpy.argmax(sred)
            #print(max)
            #print(max-(640*((max/640))))
            print(s2d[(max-640*(max/640))][max%480])
            max_x, max_y = max-640*(max/640), max%480
            pygame.surfarray.blit_array(s, s2d)
            m = pygame.mask.from_threshold(s,g, t)
            for blob in m.connected_components(10):
                coord = blob.centroid()
                pygame.draw.circle(s,r, (max_x, max_y), 50, 5)
                if (coord[0] >400):
                    if (prevDir != 'right'):
                        print('right')
                        prevDir = 'right'
                elif (coord[0] <240):
                    if (prevDir != 'left'):
                        print('left')
                        prevDir = 'left'
                else:
                    print('ontrack')
                    prevDir = 'ontrack'
        d.blit(s,(0,0))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == QUIT:
                cam.stop()
                going = False
