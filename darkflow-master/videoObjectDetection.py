#importing Necessary Libraries
import matplotlib.pyplot as plt
import numpy as np
import numpy as np
import argparse
import time
import cv2
import os
import tkinter as tk
import tkinter
import tkinter.filedialog
import os
import sys
import cv2
from darkflow.net.build import TFNet
import cv2
#Loading Model definitions in options
options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.1}
tfnet = TFNet(options)
import pprint as pp
#function to place boxes around image based on the predictions
def boxing(original_img, predictions):
    newImage = np.copy(original_img)

    for result in predictions:
        top_x = result['topleft']['x']#getting top left x co-ordinate
        top_y = result['topleft']['y']#getting top left y co-ordinate

        btm_x = result['bottomright']['x']#getting bottom right x co-ordinate
        btm_y = result['bottomright']['y']#getting bottom left y co-ordinate

        confidence = result['confidence']#calculating the confidence
        label = result['label'] + " " + str(round(confidence, 3))

        if confidence > 0.3:#confidence >30%
            newImage = cv2.rectangle(newImage, (top_x, top_y), (btm_x, btm_y), (255,0,0), 3)#Placing Rectangle around image
            #Placing text above Rectangle
            newImage = cv2.putText(newImage, label, (top_x, top_y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.8, (0, 230, 0), 1, cv2.LINE_AA)
            
    return newImage
#global panelA
path = tkinter.filedialog.askopenfilename()#video selector
w = tk.Tk()
cap = cv2.VideoCapture(path)#Capturing the video
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   #calculating width
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) #calculating height

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#saving video
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (int(width), int(height)))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if ret == True:
        frame = np.asarray(frame)
        results = tfnet.return_predict(frame)

        new_frame = boxing(frame, results)

        # Display the resulting frame
        out.write(new_frame)
        cv2.imshow('frame',new_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
w.destroy()