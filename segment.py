from SimpleCV import Image
import time

left = Image("line_left.jpg")
right = Image("line_right.jpg")
center = Image("line_center.jpg")

def segment(img, w_segments, h_segments):
    img_w, img_h = img.size()
    section_w = img_w/w_segments
    section_h = img_h/h_segments
    segments = []
    for i in range(w_segments):
        segments.append([])
        for j in range(h_segments):
            segments[i].append(img.crop(i*section_w, j*section_h, section_w, section_h))

    for i in segments:
        for j in i:
            j.show()
            time.sleep(5)

    return segments

def assign_number(segments):


segments = segment(left, 3,2)
