import cv2, time
import numpy as np

cap = cv2.VideoCapture('2.avi')


image_width = 640
scan_width, scan_height = 200, 20

lmid, rmid = scan_width, image_width - scan_width  # 모든 차로가 왼쪽으로 커브 -> rmid의 값을 lmid보다 더 줄인다.
area_width, area_height = 20, 10
roi_vertical_pos = 300
row_begin = (scan_height - area_height) // 2
row_end = row_begin + area_height
pixel_cnt_threshold = 0.15 * area_height * area_width
canny_pixel_cnt_threshold = 0.01 * area_height * area_width
roi_mid = 5



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
    lower_white = np.array([0,0,130])
    upper_white = np.array([131, 255, 255])
    mask = cv2.inRange(hsv, lower_white, upper_white)

    view2 = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)

    left, right = -1, -1

    pre_left = left
    pre_right = right

    # 안쪽에서 바깥쪽으로 검사
    for l in range(lmid, area_width, -1):
        canny_area = canny[row_begin:row_end, l-area_width:l]
        if cv2.countNonZero(canny_area) > canny_pixel_cnt_threshold:
            left = l
            print(left)
            break

    for r in range(rmid, image_width - area_width):
        canny_area = canny[row_begin:row_end, r-area_width:r]

        if cv2.countNonZero(canny_area) > canny_pixel_cnt_threshold:
            right = r
            print(right)
            break

    #오른쪽과 왼쪽 차선의 간격이 너무 좁을 때 > 이전 차선이 lost일 때 현재 차선을 lost로 지정
    if right > 0 and left > 0 and right - left < 450:
        if pre_left == -1:
            left = -1
        elif pre_right == -1:
            right = -1
    print("right: ", right)
    print("left: ", left)

    # if abs(pre_right - right) > 20:
    #     if pre_right == -1:
    #         right = -1
    #
    # elif abs(pre_left - left) > 20:
    #     if pre_left == -1:
    #         left = -1



    if left != -1:
        lsquare = cv2.rectangle(frame, (left-area_width, row_begin+roi_vertical_pos),
                                (left, row_end+roi_vertical_pos), (0,255,0), 3)
    else:
        print("Lost left line")

    if right != -1:
        rsquare = cv2.rectangle(frame, (right, row_begin+roi_vertical_pos)
                                ,(right + area_width, row_end+roi_vertical_pos)
                                ,(0,0,255), 3)
    else:
        print("Lost right line")


    # print("left: ", detect_left)
    # print("right: ", detect_right)

    cv2.imshow("origin", frame)
    cv2.imshow("hsv", canny)
    #cv2.imshow("view", view2)


    # canny -> 흰색이 발견되었을 때
    # bin > 90 이상일 때 제외

    time.sleep(0.02)






cap.release()
cv2.destroyAllWindows()


