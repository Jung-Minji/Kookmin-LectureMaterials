import cv2

vid = cv2.VideoCapture('small.avi')

while True:
    ret, frame = vid.read()
    if not ret:
        break
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret:
        cv2.imshow('video', frame)
    if cv2.waitKey(1) > 0:
        break

vid.release()
cv2.destroyAllWindows()
