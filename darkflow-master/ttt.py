import tkinter as tk
import tkinter
import tkinter.filedialog
import os
import sys
import cv2
def select_image():
 # grab a reference to the image panels
 global panelA, panelB

 # open a file chooser dialog and allow the user to select an input
 # image
 path = tkinter.filedialog.askopenfilename()

 # ensure a file path was selected
 if len(path) > 0:
    # load the image from disk, convert it to grayscale, and detect
    # edges in it
    image = cv2.imread(path)
    #image = cv2.imread("1.jpg")
    image = cv2.resize(image, None, fx=0.2, fy=0.2)
    labelsPath="cfg/coco.names"
    cfgpath="cfg/yolo.cfg"
    wpath="bin/yolo.weights"
    Lables=get_labels(labelsPath)
    CFG=get_config(cfgpath)
    Weights=get_weights(wpath)
    nets=load_model(CFG,Weights)
    Colors=get_colors(Lables)
    res=get_predection(image,nets,Lables,Colors)
    # image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    # show the output image
    cv2.imshow("Image", res)
    cv2.waitKey()
    #edged = os.path.dirname(os.path.dirname(path))
    #edged = cv2.resize(edged, dsize=(500, 600), interpolation=cv2.INTER_CUBIC)


    # OpenCV represents images in BGR order; however PIL represents
    # images in RGB order, so we need to swap the channels
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # convert the images to PIL format...
    #image = Image.fromarray(image)
    #edged = Image.fromarray(edged)

    # ...and then to ImageTk format
    #image = ImageTk.PhotoImage(image)
    #edged = ImageTk.PhotoImage(edged)

    # if the panels are None, initialize them
    #if panelA is None or panelB is None:
        # the first panel will store our original image
        #panelA = tk.Label(image=image)
        #panelA.image = image
        #panelA.pack(side="left", padx=10, pady=10)

        # while the second panel will store the edge map
        #panelB = tk.Label(image=edged)
        #panelB.image = edged
        #panelB.pack(side="right", padx=10, pady=10)

    # otherwise, update the image panels
    #else:
        # update the pannels
     #   panelA.configure(image=image)
      #  panelB.configure(image=edged)
       # panelA.image = image
        #panelB.image = edged

# initialize the window toolkit along with the two image panels
root = tk.Tk()
panelA = None
panelB = None
#print("done")

# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = tk.Button(root, text="Select an image", command=select_image)
print("done1")
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
print("done2")

# kick off the GUI
root.mainloop()
print("done3")
