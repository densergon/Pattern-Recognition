import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from matplotlib.pyplot import imread
from sklearn import preprocessing
import cv2

#Leer imagen
imgpre = cv2.imread('boscosobw.jpg')
known=[]
x=[]
y=[]
#Analiza 81 pixeles
for fila in range (216):
    for columna in range (331):
        b,g,r=imgpre[fila,columna]
        if(b==255 and g==255 and r==255):
            x.append(fila)
            y.append(columna)
            known.append('1')
        else:
            x.append(fila)
            y.append(columna)
            known.append('0')

# Lee la imagen y la guarda en una variable
img = imread('bw_image.jpg')

# Convierte la información de la imagen a una matriz
data = img.flatten()

#Este objeto sirve para darle formato a los vectores
le = preprocessing.LabelEncoder()

# Damos formato al vector de las etiqueta
labels=le.fit_transform(known)
features=list(zip(x,y))
X_train, X_test, y_train, y_test = train_test_split(features,labels, test_size=0.3)

# K-NN Clasificador con 5

knn = KNeighborsClassifier(n_neighbors=5)

#Entrenar el clasificador
knn.fit(X_train, y_train)

# Usa el clasificador para predecir
predictions = knn.predict(X_test)

# Evaluamos el rendimiento del clasificador
print(accuracy_score(y_test, predictions))