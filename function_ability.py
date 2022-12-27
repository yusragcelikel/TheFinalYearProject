import cv2
import os.path
process_choice_global = 1

def checkPerson():
    #Bu image ile kayıtlı image’ler(saved image dosyasındaki) karşılaştırılacak,
    #Görüntü %85 veya 90 üzeri eşleşiyorsa "Photo recognized. Hello eşleşen fotonun
    # başlığı !" yazacak “check-in” dosyası temizlenip program sonlandırılacak.

    #eşleşen görüntü yoksa
    process_photo(False)


def process_photo(isFound):
  if isFound == True:
    print("There is a person in file!")


  if isFound == False:
    print("There is no such person!")
    response = input("Would you like to create a record? Press Y for YES or N for NO: ")
    if response == "Y":
      # Perform steps 2, 3, 4 = called function
      saveImage(process_choice_global)
      #pass
    else:
      print("Process terminated.")
      # Clear the "check-in" file
      # Terminate the program
      pass

def selectChoice():
    print("Press 1 for the SAVE process.")
    print("Press 2 for the RECOGNIZE process.")
    process_choice_global = int(input())
    return process_choice_global

def saveImage(process_choice):

    if process_choice == 1:
        print("Please enter the admin password to continue.")
        password_counter = 0

        while password_counter < 3:  # password check
            password = int(input("Please enter the admin password: "))

            if password == 0000:
                print("Access Granted.")
                img_name = input("Please type the name: ").lower()

                cap = cv2.VideoCapture(0)  # video objectimizi oluşturduk
                print("press ESC to close")
                print("press SPACE to save image")
                img_counter = 0

                while True:
                    success, img = cap.read()

                    #if img_counter == 1:
                        #exit()  # 1 tane image capture edildiğinde programı kapatır.

                    cv2.imshow("Image", img)  # kamera görüntüsü image adlı pencerede gosterilir
                    k = cv2.waitKey(1)

                    if k % 256 == 27:
                        break  # esc tuşuna basıldığında kamera penceresi kapanacak

                    elif k % 256 == 32:
                        path = "C:/Users/oguz9/Documents/GitHub/TheFinalYearProject/pythonProject/saved_subjects"
                        cv2.imwrite(os.path.join(path, "{}.png".format(img_name)), img)

                        print("Image Successfully Captured and Saved.")
                        img_counter += 1

                break
            else:
                print("Access Denied!")
                password_counter += 1
                if password_counter == 3:
                    print("You\'ve entered the wrong password three times. Programme shutting down.")





if __name__ == "__main__":
    processChoice = selectChoice()
    saveImage(processChoice)
    checkPerson()
