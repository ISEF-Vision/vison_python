import numpy as np

SLOPE_MAX = 10000


class Line:
    def __init__(self):
        self.pt1 = (0, 0)
        self.pt2 = (0, 0)

        self.size = 0
        self.slope = 0

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = (x1, y1)
        self.pt2 = (x2, y2)

        self.size = np.sqrt((pow(x1 - x2, 2) + pow(y1 - y2, 2)))
        if x1 == x2:
            self.slope = 90
        else:
            self.slope = np.rad2deg(max(np.arctan(float(y1-y2)/float(x1-x2), SLOPE_MAX)))
        if self.slope < 0:
            self.slope = self.slope + 180


class DegreeLine:
    color_dict = {
        "vertical": (100, 0, 0),  # Dark Blue
        "left_border": (255, 0, 0),  # Blue # left_border
        "right_vector": (255, 0, 255),  # Pink # right_vector
        "horizon": (0, 255, 0),  # Green
        "right_border": (0, 0, 255),  # Red # right_border
        "left_vector": (255, 255, 255),  # White # left_vector
        "undefined": (0, 0, 0)  # Black
    }

    def __init__(self, x1, y1, x2, y2, theta):
        self.pt1 = (x1, y1)
        self.pt2 = (x2, y2)
        self.theta = theta
        self.type = self._set_line_type(theta)

    @staticmethod
    def _set_line_type(theta):
        vertical_condition = 0 < theta < 0.2 or 3.0 < theta < 3.2
        left_border_condition = 0.2 < theta < 0.8
        right_vector_condition = 0.8 < theta < 1.4
        horizon_condition = 1.4 < theta < 1.8
        left_vector_condition = 1.8 < theta < 2.4
        right_border_condition = 2.4 < theta < 3.0

        if vertical_condition:
            return "vertical"
        elif left_border_condition:
            return "left_border"
        elif right_vector_condition:
            return "right_vector"
        elif horizon_condition:
            return "horizon"
        elif left_vector_condition:
            return "left_vector"
        elif right_border_condition:
            return "right_border"
        else:
            return "undefined"
