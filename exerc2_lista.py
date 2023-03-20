import cv2

img = cv2.imread('wally.png')
cv2.imshow("Original", img)

flip_vertical = img[:,::-1]
cv2.imshow("Flip Vertical", flip_vertical)
cv2.waitKey(0)