import cv2

from recognizer import PatternRecognizer
from plot import Plot
import core.preprocessing as pre

name = "walking"
file_url = "../../test_videos/" + name + ".mp4"

cap = cv2.VideoCapture(file_url)

pattern_recognizer = PatternRecognizer()
plot = Plot(pattern_recognizer)

while cap.isOpened():
    ret, frame_origin = cap.read()
    if frame_origin is None:
        break

    frame = pre.resize(frame_origin, 0.4)
    pattern_recognizer.update(frame)

    cv2.imshow('frame', frame)

plot.save(name)
