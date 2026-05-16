from tkinter import*
from tkinter.ttk import*
from tkinter import messagebox
screen = Tk()
screen.geometry("500x350")

#functions:


myaddressbook = {}

def clear_all():
    entername.delete(0,END)
    enteraddress.delete(0,END)
    entermobile.delete(0,END)
    enteremail.delete(0,END)
    enterbirth.delete(0,END)

def updateaddressbook():
    x= entername.get()
    if x==" ":
        messagebox.showinfo("Error:","No name given")
    else:
        if x not in myaddressbook.keys():
            adbook.insert(END,x)
        myaddressbook[x] = (enteraddress.get(),entermobile.get(),enteremail.get(),enterbirth.get())#
        clear_all()

    





















#information:



adtext = Label(screen,text = "My Address Book")
adtext.place(x=130,y=20)


adbook = Listbox(screen,width = 35,height = 10)
adbook.place(x=50,y=50)


name = Label(screen,text = "Name:")
name.place(x=300,y=50)

entername = Entry(screen,width=20)
entername.place(x=350,y=50)


address = Label(screen,text = "Address:")
address.place(x=300,y=90)


enteraddress = Entry(screen,width=20)
enteraddress.place(x=350,y=90)


mobile = Label(screen,text="Mobile:")
mobile.place(x=300,y=130)

entermobile = Entry(screen,width =20)
entermobile.place(x=350,y=130)

email = Label(screen,text="Email:")
email.place(x=300,y=170)

enteremail = Entry(screen,width =20)
enteremail.place(x=350,y=170)

dateofbirth = Label(screen,text= "Birth:")
dateofbirth.place(x=300,y=210)

enterbirth = Entry(screen,width =20)
enterbirth.place(x=350,y=210)







#buttons




update = Button(screen,text="Update",command = updateaddressbook)
update.place(x=350,y=270)


edit = Button(screen,text="Edit")
edit.place(x=50,y=270)

delete = Button(screen,text="Delete")
delete.place(x=50,y=300)

save = Button(screen,text = "Save",width = 20)
save.place(x=170,y=280)

open = Button(screen,text="Open")
open.place(x=250,y=20)

mainloop()