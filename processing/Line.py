"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    > File Name: Line.py
    > Project Name: LineFittingModule_py
    > Author: Dongmin Kim
    > Purpose: 2-D line class
    > Created Time: 2017/02/27
    > Copyright (c) 2017, Dongmin Kim
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import Point

class Line:
    DIVIDOR = 1e5
    def __init__():
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def Set(x1, y1, x2, y2):
        Set(Point(x1, y1), Point(x2, y2))
        
    def Set(Point st, Point ed):
        x1 = st.x1
        y1 = st.y1
        x2 = ed.x2
        y2 = ed.y2
    def calculate():
        size = (pow(x1 - x2, 2) + pow(y1 - y2, 2)) / DIVIDOR
        if(x1 == x2)
            slope = DIVIDOR
        else
            slope = (y1 - y2) / (x1 - x2) * 180.0 / 3.14
    def getSize():
        return size
    def getSlope():
        return slope
