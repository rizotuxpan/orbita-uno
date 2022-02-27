import cv2
import numpy as np

def posicion(event, x, y, flags, param):
    print('--------------')
    print('Event=', event)
    print('x=', x)
    print('y=', y)
    print('flags=', flags)

cap = cv2.VideoCapture('rtsp://admin:C0nf1gur4c10n@10.27.67.100/profile3/media.smp')
cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', posicion)

while True:
    ret, frame = cap.read()
    if ret == False: break

    cv2.imshow('Frame', frame)
        
    k = cv2.waitKey(1) & 0xFF
    if k == 27: break

cap.release()
cv2.destroyAllWindows()