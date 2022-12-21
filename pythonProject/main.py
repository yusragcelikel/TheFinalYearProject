import os.path
from tkinter import *
import cv2
#import mediapipe as mp


#-------------the selected choice---------------
print("Press 1 for the SAVE process.")
print("Press 2 for the RECOGNIZE process.")
process_choice = int(input())
#print(process_choice)
#-------------the selected choice---------------

if process_choice == 1:

    print("Please enter the admin password to continue.")
    password_counter = 0

    while password_counter < 3:
        password = int(input("Please enter the admin password: "))

        if password == 0000:
            print("Access Granted.")
            img_name = input("Please type the name: ")

            cap = cv2.VideoCapture(0)  # video objectimizi oluşturduk
            print("press ESC to close")
            print("press SPACE to save image")
            img_counter = 0

            while True:
                success, img = cap.read()

                if img_counter == 1:
                    exit()  # 1 tane image capture edildiğinde programı kapatır.

                cv2.imshow("Image", img)  # kamera görüntüsü image adlı pencerede gosterilir
                k = cv2.waitKey(1)

                if k % 256 == 27:
                    break  # esc tuşuna basıldığında kamera penceresi kapanacak

                elif k % 256 == 32:  # boşluk tuşuna basıldığında image capture edilecek
                    #                print("Please type the image name: ")
                    #                img_name = input("Please type the image name: ")
                    #                imageFullName = ("imageName{}.png".format(img_counter))
                    #                cv2.imwrite(imageFullName, img)
                    #                cv2.imread(imageFullName, img)
                    path = "C:/Users/oguz9/Documents/GitHub/TheFinalYearProject/pythonProject/saved_subjects"
                    cv2.imwrite(os.path.join(path, "{}.png".format(img_name)), img)

                    print("Image Successfully Captured and Saved.")
                    img_counter += 1

            #                if  #image saved_object'te kayıtlı değilse(recognition yapacak) görüntüyü checkin
            # dosyasından saved_ob. dosyanına kaydedip checkin'i temizleyecek
            #               else #saved_object'te kayıtlı görüntünün ismi ekrana basılıp merhaba ... yazacak, checkin'i temizleyecek.
            #    cv2.waitKey(1)

            break
        else:
            print("Access Denied!")
            password_counter += 1
            if password_counter == 3:
                print("You\'ve entered the wrong password three times. Programme shutting down.")


elif process_choice == 2:
    print("Your choice is Recognize process")

else:
    print("You\'ve punched an invalid number.")
    exit()








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

