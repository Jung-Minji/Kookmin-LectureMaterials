import cv2, time
import numpy as np

cap = cv2.VideoCapture('2.avi')
# 막 발견한 곳에서 가까이에서 차선을 발견할 가능성이 높다.
def find_edge(edge, beg, end, height):
    if beg < end:   # 오른쪽
        r = range(beg, end)
    else:   # 왼쪽
        r = range(beg, end-1, -1)

    for h in r:
        if (edge[height, h] == 255) or (edge[height+1, h] == 255) or (edge[height-1,h] == 255):
            break
    else:
        h = -1

    return h

def check_area(img, col1, col2, scan_height, area_height, pxl_cnt_threshold):
    row1 = (scan_height - area_height) // 2
    row2 = row1 + area_height
    area = img[row1:row2, col1:col2]
    return cv2.countNonZero(area) > pxl_cnt_threshold



image_width = 640
scan_width, scan_height = 100, 20

lmid, rmid = scan_width, image_width - scan_width
area_width, area_height = 20, 10
roi_vertical_pos = 300
row_begin = (scan_height - area_height) // 2
row_end = row_begin + area_height
pixel_cnt_threshold = 0.15 * area_height * area_width
canny_pixel_cnt_threshold = 0.01 * area_height * area_width
roi_mid = 5
left = -1
right = -1


while True:
    ret, frame = cap.read()

    if not ret:
        break
    if cv2.waitKey(1) & 0xFF == 27:
        break

    roi = frame[roi_vertical_pos:roi_vertical_pos+scan_height, :]
    frame = cv2.rectangle(frame, (0, roi_vertical_pos),
                          (image_width-1, roi_vertical_pos + scan_height),
                          (255, 0, 0), 3)

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 40, 160)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_white = np.array([0,0,180])
    upper_white = np.array([131, 255, 255])
    mask = cv2.inRange(hsv, lower_white, upper_white)

    view2 = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)

    detect_left, detect_right = -1, -1


    # 차선의 스캔 범위를 동적으로 조정
    if left == -1:
        l_beg = 150
        l_end = 0
    else:
        # l_beg = min(left + area_width, image_width-1)
        # l_end = max(0, left-area_width)
        l_beg = min(left + scan_width, image_width - 1)
        l_end = max(area_width, left-scan_width)

    l = find_edge(canny, l_beg, l_end, roi_mid)

    if right == -1:
        r_beg = image_width - scan_width
        r_end = image_width-1
    else:
        # r_beg = max(right - area_width, scan_width)
        # r_end = min(right+ area_width, image_width-1)
        r_beg = max(right - scan_width, scan_width)
        r_end = min(right+ scan_width, image_width-area_width-1)


    r = find_edge(canny, r_beg, r_end, roi_mid)

    if l != -1:
        detect_left = l

    if r != -1:
        detect_right = r



    if detect_left > 0 and detect_right > 0 and detect_right - detect_left < 440:
        if left == -1:
            detect_left = -1
        elif right == -1:
            detect_right = -1


    if detect_left > 0:
        if left == -1:
            left = detect_left
        elif abs(detect_left - left) < 20:
            left = detect_left
    elif left < 2*area_width:
        left = -1

    if detect_right > 0:
        if right == -1:
            right = detect_right
        elif abs(detect_right - right) < 20:
            right = detect_right
    elif right < 2*area_width:
        right = -1


    if detect_left != -1:
        lsquare = cv2.rectangle(frame, (detect_left-area_width, row_begin+roi_vertical_pos),
                                (detect_left, row_end+roi_vertical_pos), (0,255,0), 3)
    else:
        print("Lost left line")

    if detect_right != -1:
        rsquare = cv2.rectangle(frame, (detect_right, row_begin+roi_vertical_pos)
                                ,(detect_right + area_width, row_end+roi_vertical_pos)
                                ,(0,0,255), 3)
    else:
        print("Lost right line")


    # right = detect_right
    # left = detect_left
    print("left: ", left)
    print("detect_left: ", detect_left)
    print("detect_right: ", detect_right)



    # print("left: ", detect_left)
    # print("right: ", detect_right)

    cv2.imshow("origin", frame)
    cv2.imshow("canny", canny)
    #cv2.imshow("view", view2)

    time.sleep(0.005)


cap.release()
cv2.destroyAllWindows()


