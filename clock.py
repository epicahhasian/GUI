from tkinter import*
from tkinter.ttk import* 
from time import strftime 



screen = Tk()
screen.title("Current Time")


currenttime = Label(screen,background="Blue",font=("Arial",30))
currenttime.pack(anchor="center")

def converttime():
    format = strftime("%H:%M:%S:%p")
    currenttime.config(text=format)
    currenttime.after(1,converttime)
    


converttime()

mainloop()

