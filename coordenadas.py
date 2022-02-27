import cv2
import numpy as np
cad = '['
def posicion(event, x, y, flags, params):
    global cad
    if event == cv2.EVENT_LBUTTONDOWN:
        cad += f'[{x},{y}],'

imagen = cv2.imread('XA0041FIJA1.jpg')
cv2.namedWindow('imagen')
cv2.setMouseCallback('imagen', posicion)
cv2.imshow('imagen', imagen)
cv2.waitKey(0)
cad=cad[:-1]
cad += ']'
print(cad)
cv2.destroyAllWindows()