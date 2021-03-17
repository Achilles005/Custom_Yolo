from tkinter import *
import tkinter
import numpy as np
import argparse
import time
import cv2
import os

confthres=0.5
nmsthres=0.1
yolo_path="./"

class MyWindow:
    
    def __init__(self, win):
        self.lbl1=Label(win, text='Object Detection')
        self.lbl2=Label(win, text='Motion Detection')
        self.lbl3=Label(win, text='Cam Object Detection')
        self.lbl4=Label(win, text='Video Object Detection')
        self.t1=Entry()
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()
        self.btn1 = Button(win, text='Object Detection')
        self.btn2=Button(win, text='Motion Detection')
        self.btn3=Button(win, text='WebCam Object Detection')
        self.btn4=Button(win,text='Video Object Detection')
        #self.lbl1.place(x=100, y=50)
        #self.t1.place(x=200, y=50)
        #self.lbl2.place(x=100, y=100)
        #self.t2.place(x=200, y=100)
        #self.lbl3.place(x=100, y=150)
        #self.t3.place(x=200, y=100)
        #self.lbl4.place(x=100, y=200)
        #self.t4.place(x=200, y=100)
        self.b1=Button(win, text='Object Detection', command=self.ObjectDetection)
        self.b2=Button(win, text='WebCam Motion Detection',command=self.MotionDetection)
        self.b3=Button(win, text='WebCam Object Detection',command=self.webCamDetection)
        self.b4=Button(win,text='Video Object Detection',command=self.VoD)
        #self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=100, y=100)
        self.b2.place(x=100, y=150)
        self.b3.place(x=100, y=200)
        self.b4.place(x=100, y=250)
        #self.lbl3.place(x=100, y=200)
        #self.t3.place(x=200, y=200)
    def webCamDetection(self):
        import camdetect
    def ObjectDetection(self):
        import objectDetection
    def MotionDetection(self):
        import detection
    def VoD(self):
        import videoObjectDetection
        

window=tkinter.Tk()
mywin=MyWindow(window)
window.title('Detections')
window.geometry("400x300+10+10")
window.mainloop()
