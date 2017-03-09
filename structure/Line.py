import numpy as np

# Define Value
DIVIDOR = 1e5


class Line:
    def __init__(self):
        self.pt1 = (0, 0)
        self.pt2 = (0, 0)

        self.size = 0
        self.slope = DIVIDOR

    def __init__(self,x1,y1,x2,y2):
        self.pt1 = (x1,y1)
        self.pt2 = (x2,y2)

        self.size = (pow(x1 - x2, 2) + pow(y1 - y2, 2)) / DIVIDOR
        if x1 == x2:
            self.slope = DIVIDOR
        else:
            self.slope = (y1 - y2) / (x1 - x2) * 180.0 / 3.14


class DegreeLine:

    color_dict ={
        "vertical":(255,0,0),
        "top_top":(255,255,0),
        "top_down":(255,0,255),
        "horizon":(0,255,0),
        "down_down":(0,255,255),
        "down_top":(255,255,255),
        "undefined":(0,0,0)
    }
    line_type=None

    def __init__(self,x1,y1,x2,y2,theta):
        self.pt1 = (x1, y1)
        self.pt2 = (x2, y2)
        self.theta = theta
        self.line_type = self.setLineType(theta)

    def setLineType(self,theta):
        vertical_condition = (0<theta and theta<0.2) or (3.0<theta and theta<3.2)
        top_top_condition = (0.2<theta and theta<0.8)
        top_down_condition = (0.8 < theta and theta<1.4)
        horizon_condition = (1.4<theta and theta<1.8)
        down_top_condition = (1.8<theta and theta<2.4)
        down_down_condition = (2.4<theta and theta<3.0)

        if(vertical_condition):
            return "vertical"
        elif(top_top_condition):
            return "top_top"
        elif(top_down_condition):
            return "top_down"
        elif(horizon_condition):
            return "horizon"
        elif(down_top_condition):
            return "down_top"
        elif(down_down_condition):
            return "down_down"
        else:
            return "undefined"