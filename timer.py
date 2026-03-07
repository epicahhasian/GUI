from tkinter import*
from tkinter import messagebox
from time import time 

screen = Tk()
screen.geometry ("200x100")
screen.title("timer")

hour = StringVar()
minute = StringVar()
second = StringVar()


hour.set ("00")
minute.set("00")
second.set("00")



hourbox = Entry(screen,textvariable = hour,width=3)
hourbox.place(x=50,y=30)

minutebox = Entry(screen,textvariable=minute,width=3)
minutebox.place(x=70,y=30)


secondbox = Entry(screen,textvariable= second,width = 3)
secondbox.place(x=90,y=30)


def convert():
    try:
        timegiven = int(hour.get())*3600+int(minute.get())*60+int(second.get())
    except:
        print("Please input a valid time")
    
    while timegiven>-1:
        min,secs=divmod(timegiven,60)

    h=00
    if min>60:
        h,min=divmod(timegiven,60)
    hour.set("{00:2d}".format(h))
    minute.set("{00:2d}".format(min))
    second.set("{00:2d}".format(secs))
    screen.update()
    time.sleep(1)
    if timegiven== 00:
        messagebox.showinfo("Time Ended","Times up")
    
    timegiven -=1



start = Button(screen,text="Start time",command =convert)
start.place(x=50,y=70)



mainloop()