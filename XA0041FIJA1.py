import cv2
import numpy as np

cap = cv2.VideoCapture('rtsp://admin:C0nf1gur4c10n@172.21.5.172/profile3/media.smp')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

while True:
    ret, frame = cap.read()
    if ret == False: break
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.rectangle(frame, (0,0), (frame.shape[1],40), (0,0,0), -1)
    color = (0,255,0)
    texto_estado = "Estado: No se ha detectado movimiento"
    cv2.putText(frame, texto_estado, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    area_pts= np.array([[7,513],[1207,215],[1275,244],[1275,431],[1130,718],[4,705]], np.int32)

    imAux = np.zeros(shape=(frame.shape[:2]), dtype=np.uint8)
    imAux = cv2.drawContours(imAux, [area_pts], -1, (255), -1)
    image_area = cv2.bitwise_and(gray, gray, mask=imAux)
    fgmask = fgbg.apply(image_area)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.dilate(fgmask, None, iterations=3)

    cnts = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for cnt in cnts:
        if cv2.contourArea(cnt) > 600:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            texto_estado="Estado: Movimiento detectado"
            cv2.rectangle(frame, (0,0), (frame.shape[1],40), (0,0,0), -1)
            color=(0,0,255)
            cv2.putText(frame, texto_estado, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.drawContours(frame, [area_pts], -1, color, 2)

    cv2.imshow('Frame', frame)
        
    k = cv2.waitKey(1) & 0xFF
    if k == 27: break

cap.release()
cv2.destroyAllWindows()