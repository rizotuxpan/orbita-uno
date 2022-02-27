import cv2
import numpy as np

def posicion(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('x=', x, ', y=', y)

cap = cv2.VideoCapture('rtsp://admin:C0nf1gur4c10n@172.21.5.172/profile3/media.smp')
cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', posicion)

while True:
    ret, frame = cap.read()
    if ret == False: break

    cv2.imshow('Frame', frame)
    if cv2.imwrite("XA0041FIJA1.jpg",frame):
        break

cap.release()
cv2.destroyAllWindows()