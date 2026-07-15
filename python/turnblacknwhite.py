import cv2
im_gray = cv2.imread('cielocolor.png', cv2.IMREAD_GRAYSCALE)
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite('cielobw.jpg', im_bw)