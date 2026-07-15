import cv2

def coordinates(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)


imagen = cv2.imread('bw_image.jpg',1) 
cv2.cvtColor(imagen,cv2.COLOR_BGRA2GRAY)
cv2.namedWindow('image')
cv2.imshow('image',imagen)
cv2.setMouseCallback('image',coordinates)
cv2.waitKey(0)
cv2.destroyAllWindows()