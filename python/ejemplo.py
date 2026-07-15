import cv2
import numpy as np

pixeles=[]
rgb=[]

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global img
    if event == cv2.EVENT_LBUTTONDBLCLK:
        pixeles.append([x,y])
        b, g, r = img[x,y]
        rgb.append([r,g,b])

# Create a black image, a window and bind the function to window
img = cv2.imread('bw_image.jpg',1)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
print(rgb)
