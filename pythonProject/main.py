from tkinter import *

















#----------------window function that closes itself in 3 second-------------
def OpenWindow():
    window = Tk()
    windowTitle = input("Please type the image title: ")
    window.title(windowTitle)

    window.configure(width=500, height=300)
    window.configure(bg='lightgray')  # window color is lightgray

    window.after(3000, lambda: window.destroy())  # Destroy the widget after 30 seconds
    window.mainloop()

test = OpenWindow()
#-------------------------------------------------------------------------------

