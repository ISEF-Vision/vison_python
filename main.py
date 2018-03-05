import cv2

from core.linear.recognizer import LinearRecognizer
from core.pattern.recognizer import PatternRecognizor
import core.preprocessing as pre

name = "walking"
file_url = "./test_videos/" + name + ".mp4"

cap = cv2.VideoCapture(file_url)
linear_recog = LinearRecognizer()
pattern_recog = PatternRecognizor()


while cap.isOpened():
    ret, frame = cap.read()
    if frame is None:
        break

    frame = pre.resize(frame,0.4)
    linear_recog.update(frame)
    pattern_recog.update(frame)
    cv2.waitKey(1)

cv2.waitKey(0)
