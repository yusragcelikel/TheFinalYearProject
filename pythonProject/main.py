from tkinter import *
import cv2
#import mediapipe as mp

print("Press 1 to SAVE process.")
print("Press 2 to RECOGNIZE process.")
process_chose = input()



cap = cv2.VideoCapture(0) #video objectimizi oluşturduk
print("press ESC to close")
print("press SPACE to save image")
img_counter = 0


while True:
    success, img = cap.read()

    if img_counter == 3:
        exit()

    cv2.imshow("Image", img)  # kamera görüntüsü image adlı pencerede gosterilir
    k = cv2.waitKey(1)

    if k%256 == 27:
        break
    elif k%256 == 32:
#        print("Please type the image name: ")
#        img_name = input("Please type the image name: ")
        imageFullName = ("imageName{}.png".format(img_counter))
        cv2.imwrite(imageFullName, img)
        print("image captured")
        img_counter += 1

#    cv2.waitKey(1)







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

