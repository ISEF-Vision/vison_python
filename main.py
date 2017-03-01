import cv2
import processing.preprocessing as pre

file_url = "../test_videos/walking.mp4"

cap = cv2.VideoCapture(file_url)

while(cap.isOpened()):
    ret,frame_origin = cap.read()
    if frame_origin ==None:
        break

    #1. Frame Resizing
    frame = pre.resize(frame_origin,0.4)
    #2. Get HoughLines
    houghlines = pre.getHoughLines(frame,80)


    #Apply Algorithm on this part


    #Draw lines
    for line in houghlines:
        cv2.line(frame,line.pt1,line.pt2,(0,0,255),2)

    cv2.imshow('frame',frame)
    cv2.waitKey(1)
