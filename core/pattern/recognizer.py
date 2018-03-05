from structure.frame_data import FrameData
import core.preprocessing as pre
from plot import Plot
import cv2


class PatternRecognizer:
    def __init__(self, plot=True):
        self.index = 2
        self.lines = {
            "left_border": {
                "array": [0],
                "avg_array": [0],
            },
            "right_vector": {
                "array": [0],
                "avg_array": [0],
            },
            "horizon": {
                "array": [0],
                "avg_array": [0],
            },
            "right_border": {
                "array": [0],
                "avg_array": [0]
            },
            "left_vector": {
                "array": [0],
                "avg_array": [0],
            }
        }
        self.sum_line_size = 30
        self.cnt = 1
        self.isplot = plot
        self.plot = Plot(self)

    def update(self, frame):
        hough_lines = pre.get_hough_lines(frame, 200)
        if len(hough_lines) > self.sum_line_size / self.cnt * 2:
            return
        else:
            self.sum_line_size += len(hough_lines)

        frame_data = FrameData(hough_lines)
        for key, value in frame_data.counts.items():
            if key == 'undefined' or key == 'vertical':
                continue

            self.lines[key]["array"].append(self.lines[key]["array"][-1] + value)

            if self.index > 21:
                array_range = self.lines[key]["array"][self.index - 21:self.index - 11]
                self.lines[key]["avg_array"].append((array_range[9] - array_range[0]) / 10)

            else:
                array_range = self.lines[key]["array"]
                self.lines[key]["avg_array"].append((array_range[self.index - 2] - array_range[0]) / (self.index - 1))

        self.index += 1
        self.draw_hough(frame, hough_lines)
        if self.isplot:
            self.plot.update()

    def draw_hough(self, frame, hough_lines):
        for line in hough_lines:
            if line.type != "vertical" and line.type != "undefined":
                cv2.line(frame, line.pt1, line.pt2, (255, 255, 255))
        cv2.imshow("hough Lines", frame)

    def clear(self):
        self.__init__()

    def get_lines(self):
        return self.lines
