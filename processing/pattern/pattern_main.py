import cv2

from recognizor import PatternRecognizor
from plot import Plot
import processing.preprocessing as pre

name= "singyan"
file_url = "../../test_videos/"+name+".mp4"

cap = cv2.VideoCapture(file_url)

sum_line_size = 30
frame_count = 1
pattern_recognizor = PatternRecognizor()
plot = Plot(pattern_recognizor)

while cap.isOpened():
    ret,frame_origin = cap.read()
    if frame_origin is None:
        break

    # 1. Resizing
    frame = pre.resize(frame_origin,0.4)

    # 2-1. Get hough lines
    hough_lines = pre.get_hough_lines(frame,200)
    if len(hough_lines) > sum_line_size/frame_count * 2:
        continue
    else:
        sum_line_size += len(hough_lines)

    # Draw lines for HoughLine
    for line in hough_lines:
        if line.type != "vertical" and line.type!= "undefined":
            cv2.line(frame,line.pt1,line.pt2,line.color_dict[line.type],2)

    pattern_recognizor.update(hough_lines)
    plot.update()

    cv2.imshow('frame',frame)

    if frame_count == 1:
        cv2.waitKey(1000)
    else:
        cv2.waitKey(1)

    frame_count += 1

plot.save(name)