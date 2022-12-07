from tkinter import *
import cv2
import mediapipe as mp


capture = cv2.VideoCapture(2)

#cv2.namedWindow("Capture Image Through Webcam")


import cv2

cap = cv2.VideoCapture(0) #video objectimizi oluşturduk

while True:
    success, img = cap.read()


    cv2.imshow("Image", img)  # kamera görüntüsü image adlı pencerede gosterilir
    cv2.waitKey(1)







#----------------window function that closes itself in 3 second-------------
#def OpenWindow():
#    window = Tk()
#    windowTitle = input("Please type the image title: ")
#    window.title(windowTitle)
#
#    window.configure(width=500, height=300)
#    window.configure(bg='lightgray')  # window color is lightgray
#
#    window.after(3000, lambda: window.destroy())  # Destroy the widget after 30 seconds
#    window.mainloop()
#
#test = OpenWindow()
#-------------------------------------------------------------------------------

