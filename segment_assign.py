from SimpleCV import Image
from SimpleCV import Color
import time

left = Image("line_left.jpg")
right = Image("line_right.jpg")
center = Image("line_center.jpg")

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
            



segments = segment(center, 3,2)
left_segments = segment(left, 3,2)
right_segments = segment(right, 3,2)
print("Center picture is classified as " + assign_number(segments))
print("Left picture is classified as " + assign_number(left_segments))
print("Right picture is classified as " + assign_number(right_segments))
