import numpy as np
import cv2

capture = cv2.VideoCapture(0) 
alpha = 1.5
beta = 125
while (1): 
	
	val, frame = capture.read()
	
	ColorBright = cv2.addWeighted(frame,alpha, np.zeros(frame.shape, frame.dtype), 0, beta)
    
	cv2.imshow('Gambar Terang', ColorBright)

	if cv2.waitKey(1) & 0xFF == ord('c'):
		break

cv2.destroyAllWindows()
capture.release()