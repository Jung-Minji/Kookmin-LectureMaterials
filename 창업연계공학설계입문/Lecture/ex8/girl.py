import cv2

img = cv2.imread('girl.png', cv2.IMREAD_GRAYSCALE)

canny = cv2.Canny(img, 50, 100)
cv2.imshow('My Girl', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
