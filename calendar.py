from tkinter import* 
import calendar

screen = Tk()
screen.title("Calendar")
screen.geometry("250x140")

ca = Label(screen,text="Calendar", fg="Red")
insertyear =Entry(screen,width = 30)

Exit = Button(screen,text="Exit",command = exit)

ca.grid (row =10 , column = 10)
Exit.grid(row= 15, column =500)
insertyear.grid(row=15,column=10)


def box():
    cascreen = Tk()
    cascreen.title("CalendarForYear")
    cascreen.geometry ("450x300")

    gethere= int(insertyear.get())
    content = calendar.calendar(gethere)


    calendaryear = Label(cascreen,text= content)
    calendaryear.grid(row=5,column= 1)


    cascreen.mainloop()



showcalendar = Button(screen,text = "Show Calendar",command=box).place(x=50,y=50)


screen.mainloop()

