import cv2

import processing.linear.regression_process as reg
import processing.preprocessing as pre

file_url = "../../test_videos/walking.mp4"

cap = cv2.VideoCapture(file_url)

while(cap.isOpened()):
    ret,frame_origin = cap.read()
    if frame_origin ==None:
        break

    # 1. 프레임 크기 조정
    frame = pre.resize(frame_origin,0.4)

    # 2-1. Get Hough Lines
    # def getHoughLines(frame, minLineLength = 100, maxLineGap = 10)
    hough_lines = pre.get_hough_lines(frame,200)

    # 2-2 Get HoughP Lines
    # def getHoughPLines(frame, minLineLength=100, maxLineGap=10):
    houghp_lines = pre.get_hough_p_lines(frame)

    # Apply Algorithm on this part

    # Draw lines for HoughLine
    for line in hough_lines:
        cv2.line(frame,line.pt1,line.pt2,line.color_dict[line.line_type],2)

    reg.regression_process(frame_origin,houghp_lines)

    cv2.imshow('frame',frame)
    cv2.waitKey(1)
