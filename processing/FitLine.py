"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    > File Name: FitLine.py
    > Project Name: LineFittingModule_py
    > Author: Dongmin Kim
    > Purpose: Fitting given Lines
    > Created Time: 2017/02/27
    > Copyright (c) 2017, Dongmin Kim
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import copy
from Line import *

class FitLine:
    def __init__():
        ## Do nothing
    
    def __init__(lines, direction):
        m_lines = copy.deepcopy(lines)
        ImgDirection = direction

    def CompareLines():
        MAX_VAL = -1
        
        preSet()

        for i in range(0, m_lines.size()):
            for j in range(0, m_lines.size()):
                if(i == j) : continue
                lossMatrix[i][j] = getLossFunc(m_lines[i]),m_lines[j])
                if(lossMatrix[i][j] > MAX_VAL):
                    MAX_VAL = lossMatrix[i][j]
                    resultLine.first = m_lines[i]
                    resultLine.second = m_lines[j]
        return resultLine

    def getLossFunc(x, y):
        xSlope = x.getSlope(), ySlope = y.getSlope()
        xSize = x.getSize(), ySize = y.getSize()

        if(abs(xSlope - ySlope) < SLOPE_DIFF_MIN):
            return -1
        return param_beta * (pow(xSize + ySize,2) - SquareLineSize) - getDiscriminant(x, y)

    def getDiscriminant(x, y):
        return -1 * abs(tan((x.slope + y.slope) / 2 - ImgDirection)

    def preSet():
        Length_sum = 0, Slope_sum = 0
        numertor = 0, denominator = 0

        for i in range(0, m_lines.size()):
            LineSize += m_lines[i].getSize()
            SquareLineSize += pow(m_lines[i].getSize(), 2)
        
        for i in range(0, m_lines.size()):
            for j in range(0, m_lines.size()):
                Length_sum += pow(m_lines[i].getSize() + m_lines[j].getSize(), 2)
                Slope_sum += getDiscriminant(m_lines[i], m_lines[j])

        Length_sum -= SquareLineSize * pow(m_lines.size(), 2)

        for i in range(0, m_lines.size()):
            for j in range(0, m_lines.size()):
                numerator += (Slope_sum - getDiscriminant(m_Lines[i], m_Lines[j]) * pow(N, 2)) * 
					(pow(N,2) * pow(m_lines[i].getSize() + m_lines[i].getSize(), 2) - Length_sum)
				denominator += pow(pow(N, 2) * pow(m_lines[i].getSize() + m_lines[i].getSize(), 2) - Length_sum, 2)

        param_beta = numerator / denominator