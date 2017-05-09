import cv2
import numpy as np
import fitline
import core.preprocessing as pre


class LinearRecognizor:
    def __init__(self):
        self.frame_width = 0
        self.frame_height =0
        self.stack_line = None
        self.cnt = 0
        self.slope_sum = 0
        self.slope_cnt = 0

    def update(self, frame):
        if self.cnt == 0:
            self.frame_width, self.frame_height = frame.shape[:2]
            self.clear()

        houghp_lines = pre.get_hough_p_lines(frame)

        first_line, second_line = self._get_two_lines(frame, houghp_lines)
        cv2.line(self.stack_line, first_line.pt1, first_line.pt2, 255, 2)
        cv2.line(self.stack_line, second_line.pt1, second_line.pt2, 255, 2)
        self.draw(first_line, second_line)

        if first_line is None:
            return

        self.slope_sum += first_line.slope + second_line.slope
        self.slope_cnt += 2
        self.cnt += 1

        if self.cnt % 30 == 0 and self.cnt != 0:
            self._get_slope()
            self.clear()

    def _get_slope(self):
        slope = self.slope_sum / float(self.slope_cnt)
        theta = np.tan(slope / 180 * 3.14)

        # Line Drawing
        if abs(theta) < 0.0:
            print "Error"
        else:
            if self.frame_height / 2.0 - float(self.frame_width) / 2.0 / float(theta) < 0:
                res = 0
            else:
                res = self.frame_height / 2.0 - float(self.frame_width) / 2.0 / float(theta)
            if self.frame_height / 2.0 + float(self.frame_width) / 2.0 / float(theta) > self.frame_width - 1:
                res2 = self.frame_width - 1
            else:
                res2 = self.frame_height / 2.0 + float(self.frame_width) / 2.0 / float(theta)

        result = np.zeros((self.frame_width, self.frame_height, 1), np.uint8)
        cv2.line(result, (int(res), 0), (int(res2), self.frame_width - 1), 255, 2)
        cv2.imshow("line slope", result)

    def _get_two_lines(self, frame, houghlines):
        origin_height, origin_width = frame.shape[:2]
        regression_background = np.zeros((origin_height, origin_width, 1), np.uint8)

        for line in houghlines:
            cv2.line(regression_background, line.pt1, line.pt2, 255, 2)

        ctr = np.array(regression_background).reshape((-1, 1, 2)).astype(np.int32)
        [vx, vy, x, y] = cv2.fitLine(ctr, cv2.DIST_L2, 0, 0.01, 0.01)

        theta = vy / vx
        first_line, second_line = fitline.FitLine(houghlines, theta * 180 / 3.14).get_compare_lines()

        if first_line is None or second_line is None:
            return None

        return first_line, second_line

    def clear(self):
        self.stack_line = np.zeros((int(self.frame_width), int(self.frame_height), 1), np.uint8)
        self.slope_sum = 0
        self.slope_cnt = 0

    def draw(self, first_line, second_line):
        cv2.imshow("stack", self.stack_line)

        two_lines_mat = np.zeros((int(self.frame_width), int(self.frame_height), 1), np.uint8)
        cv2.line(two_lines_mat, first_line.pt1, first_line.pt2, 255, 2)
        cv2.line(two_lines_mat, second_line.pt1, second_line.pt2, 255, 2)
        cv2.imshow("two lines", two_lines_mat)
