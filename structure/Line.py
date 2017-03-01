import numpy as np
class Line:
    def __init__(self,x1,y1,x2,y2):
        self.pt1 = (x1,y1)
        self.pt2 = (x2,y2)


class DegreeLine:
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