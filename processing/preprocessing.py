import cv2
import numpy as np
import structure.Line as Line

# Define values
houghline_threshold = 150

# -------------------
# fucntion resize
# Params : frame origin, resizing value
# Return : Resized Frames
# Aim for resizing frames more easily
# -------------------


def resize(frame_origin,resize=0.4):

    height, width = frame_origin.shape[:2]
    frame = cv2.resize(frame_origin, (int(width * resize), int(height * resize)), interpolation=cv2.INTER_CUBIC)
    return frame


# -------------------
# function : get_hough_p_lines
# Params : frame origin, minLineLength value, maxLineGape value
# Return : hough lines
# Return the opencv hough line p function's lines
# -------------------


def get_hough_p_lines(frame,minLineLength=100,maxLineGap=10):
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    canny = cv2.Canny(gray, 100, 200, apertureSize=3)
    lines_data = cv2.HoughLinesP(canny, 1, np.pi / 180, 100, minLineLength, maxLineGap)
    lines = []
    for line_data in lines_data:
        x1, y1, x2, y2 = line_data[0]
        line = Line.Line(x1,y1,x2,y2)
        lines.append(line)
    return lines


# -------------------
# function : get_hough_lines
# Params : frame origin, resizing value
# Return : hough lines
# Return the opencv hough line p function's lines and classified result
# -------------------


def get_hough_lines(frame,canny_threshold=100,max_line_size=50,min_line_size=40):

    global houghline_threshold
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    canny = cv2.Canny(gray, canny_threshold, 200, apertureSize=3)
    cv2.imshow("canny",canny)

    lines_data = cv2.HoughLines(canny, 1, np.pi / 180, houghline_threshold)
    lines =[]
    if lines == None:
        pass
    else:
        for data in lines_data:
            rho, theta = data[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            line = Line.DegreeLine(x1,y1,x2,y2,theta)
            lines.append(line)

    # print "line size " + str(len(lines))

    if (len(lines) < min_line_size):
        houghline_threshold -= 10
    if (len(lines) > max_line_size):
        houghline_threshold += 5
    print "size:" + str(len(lines)) + " threshold:" + str(houghline_threshold)

    return lines
