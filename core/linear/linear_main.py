import cv2
import core.preprocessing as pre
import recognizer

name = "walking"
file_url = "../../test_videos/" + name + ".mp4"

cap = cv2.VideoCapture(file_url)
recognizer = recognizer.LinearRecognizer()

while cap.isOpened():
    ret, frame_origin = cap.read()
    frame = pre.resize(frame_origin, 0.4)
    if frame is None:
        break
    recognizer.update(frame)

    cv2.imshow('frame', frame)
    cv2.waitKey(33)
