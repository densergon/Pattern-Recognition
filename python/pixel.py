#Importar librería cv2
import cv2

#Leer imagen
img = cv2.imread('bw_image.jpg')
known=[]
#Analiza 81 pixeles
for fila in range (224):
    for columna in range (224):
        b,g,r=img[fila,columna]
        if(b==255 and g==255 and r==255):
            known.append('1')
        else:
            known.append('0')