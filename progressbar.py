from tkinter import*
from tkinter.ttk import* 
import time 
bar = Tk()

widget = Progressbar(bar,orient=HORIZONTAL,length=1005,mode="determinate")

def progress():
    widget["value"] = 20 
    bar.update_idletasks()
    time.sleep (1)
    widget ["value"] = 40 
    bar.update_idletasks()
    time.sleep (1)
    widget ["value"] = 50 
    bar.update_idletasks()
    time.sleep (1)
    widget ["value"] = 70 
    bar.update_idletasks()
    time.sleep (1)
    widget["value"] = 90 
    bar.update_idletasks()
    time.sleep (1)
    widget["value"] = 100 
    bar.update_idletasks()


widget.pack(padx = 50, pady = 100)

start = Button(bar,text="Start",command=progress).pack(padx = 30, pady=100)






#spinbox


spinbox = Spinbox(bar,from_=1,to = 100).pack(padx = 20, pady = 100)


mainloop()
