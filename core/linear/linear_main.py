import cv2
import core.preprocessing as pre
import recognizor

name = "walking"
file_url = "../../test_videos/" + name + ".mp4"

cap = cv2.VideoCapture(file_url)
recognizor = recognizor.LinearRecognizor()

while (cap.isOpened()):
    ret, frame_origin = cap.read()
    frame = pre.resize(frame_origin, 0.4)
    if frame is None:
        break
    recognizor.update(frame)

    cv2.imshow('frame', frame)
    cv2.waitKey(33)
