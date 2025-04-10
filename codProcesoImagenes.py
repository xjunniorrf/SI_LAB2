import numpy as np
import cv2

img = cv2.imread('E:/UCV_7 CICLO/SISTEMAS INTELIGENTES/SEMANA 2/SI_LAB2/ImagenPNG.png')
pixeles = (400, 400)
tamañoImagen = cv2.resize(img,pixeles, interpolation=cv2.INTER_AREA)
cv2.imshow('imagen', tamañoImagen) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
