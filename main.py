import easyocr
import matplotlib.pyplot as plt
import cv2
import time
import numpy as np

reader = easyocr.Reader(['en'], gpu=True)
vid = cv2.VideoCapture ("numplate.mp4")
#vid = cv2.VideoCapture (8)
skip_frame = True

while(True):
     a = time.time()
     ret, img = vid.read()

     gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
     result = reader.readtext(gray)
     text = ""

     for res in result:
        text += res[1] + " "
     cv2.putText(img, text, (58,78), cv2.FONT_HERSHEY_SIMPLEX, 1, (58,58,255), 2)

     ##FPS
     b= time.time()
     fps =1/(b-a)
     cv2.line(img, (28,25), (127,25),[85_45_255],38)
     cv2.putText(img, f'(FPS): (int(fps))', (58, 78), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, lineType=cv2.LINE_AA)
     cv2.imshow("result", img)

     if cv2.waitKey(1) & 0xFF== ord('a'):
         break
     print (fps)
     print(text)