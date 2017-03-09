import numpy as np
import cv2


def regression_process(frame_origin, houghlines, ):

    height, width = frame_origin.shape[:2]
    regression_background = np.zeros((int(height * 0.4), int(width * 0.4), 1), np.uint8)
    regression_result = np.zeros((int(height * 0.4), int(width * 0.4), 1), np.uint8)

    # Draw lines for HoughLineP
    for line in houghlines:
        cv2.line(regression_background, line.pt1, line.pt2, 255, 2)

    cv2.imshow("regression",regression_background)

    # then apply fitline() function
    ctr = np.array(regression_background).reshape((-1, 1, 2)).astype(np.int32)
    [vx, vy, x, y] = cv2.fitLine(ctr, cv2.DIST_L2, 0, 0.01, 0.01)

    theta = vy/vx
    rows, cols = regression_background.shape[:2]
    # Now find two extreme points on the line to draw line
    lefty = int((-x * vy / vx) + y)
    righty = int(((cols - x) * vy / vx) + y)

    cv2.line(regression_result, (cols - 1, righty), (0, lefty), 255, 2)
    cv2.imshow("regression_result",regression_result)


    cv2.waitKey(1)