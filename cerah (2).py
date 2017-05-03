
import numpy as np
import cv2

capture = cv2.VideoCapture(0) 

while (1): 
	
	val, frame = capture.read()
	
	abu = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	negative = (255 - abu)
	
	cv2.imshow('Gambar Negatif', negative)
	if cv2.waitKey(1) & 0xFF == ord('c'):
		break

cv2.destroyAllWindows()
capture.release()