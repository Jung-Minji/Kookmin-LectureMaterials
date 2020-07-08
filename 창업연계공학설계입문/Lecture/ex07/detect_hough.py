#!/usr/bin/env python

import cv2, time
import numpy as np
import math
# vertics = np.array([[(1, 400),(640, 400),(550, 300), (350, 300)]], dtype=np.int32)


# ro = roi(hsv, vertics)

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img,mask)
    return masked

cap = cv2.VideoCapture('2.avi')

value_threshold = 60

image_width = 640
scan_width, scan_height = 200, 20
lmid, rmid = scan_width, image_width - scan_width
area_width, area_height = 20, 10
roi_vertical_pos = 430
row_begin = (scan_height - area_height) // 2
row_end = row_begin + area_height
canny_pixel_cnt_threshold = 0.01 * area_width * area_height

import numpy as np
import math

def angle(dx, dy):
    return math.atan2(dy, dx) * 180 / math.pi


#vertics = np.array([[(1, 400), (640, 400), (630, 300), (30, 300)]], dtype=np.int32)


# ro = roi(hsv, vertics)

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img,mask)
    return masked

while True:
    ret, frame = cap.read()
    if not ret:
        break
    if cv2.waitKey(1) & 0xFF == 27:
        break

    # vertics = np.array([[(0, 400), (0, 450), (200, 200), (440, 200), (640, 450), (640, 400)],], dtype=np.int32)
    vertics = np.array([[(0, 450), (0, 400), (200, 200), (440, 200), (640, 400), (640, 450)], ], dtype=np.int32)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    r = roi(gray, vertics)
    dst = cv2.Canny(r, 50, 200)
    hsv = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
    row, col, ch = frame.shape


    lines = cv2.HoughLinesP(dst, 1, math.pi / 180.0, 90, minLineLength=50, maxLineGap=18)
    left, right = -1, -1

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            frame = cv2.line(hsv, (x1, y1), (x2, y2), (51, 204, 255), 5)
            if angle(y2 - y1, x2 - x1) == 0:
                continue

            elif 100 < angle(y2 - y1, x2 - x1) < 135 :
                print("left: ", round(angle(y2 - y1, x2 - x1)))
                cv2.line(hsv, (x1, y1), (x2, y2), (255, 0, 0), 3)
                left = round(angle(y2 - y1, x2 - x1))
                print("left angle: ", (x2-x1) // (y2-y1))

            elif  80 > angle(y2 - y1, x2 - x1) > 45:
                print("right: ", round(angle(y2 - y1, x2 - x1)))
                cv2.line(hsv, (x1, y1), (x2, y2), (0, 0, 255), 3)
                right = round(angle(y2 - y1, x2 - x1))
                print("right angle: ", (x2-x1) // (y2-y1))

    if  120 >= left >= 110 or 70 > right >= 60:
        print("go straight")

    elif right >= 70:
        print("go left")
    elif  99 < left < 110:
        print("go right")

    cv2.imshow("hough", hsv)
    cv2.imshow("origin", frame)

    time.sleep(0)

cap.release()
cv2.destroyAllWindows()
