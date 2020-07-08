import cv2

cap = cv2.VideoCapture('small.avi')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    if ret:
        cv2.imshow('black', frame)

    if cv2.waitKey(100) > 0:
        break

cap.release()
cv2.destroyAllWindows()