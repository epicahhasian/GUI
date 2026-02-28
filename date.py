from tkinter import*
from tkinter.ttk import*
from time import strftime 



screen = Tk()
screen.title("Current Date")


currentdate = Label(screen,background = "Purple",font =("Arial",30))
currentdate.pack(anchor="center")


def date():
    format = strftime("%B/%d/%Y")
    currentdate.config(text=format)
    currentdate.after(1,date)



date()
mainloop()