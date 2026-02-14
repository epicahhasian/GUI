from tkinter import*


screen = Tk()
screen.title("Weight Converter")
screen.geometry("500x300")



def getweight():
    store = float(enter.get())*1000
    store2 = float(enter.get())*2.20462
    store3= float(enter.get())*35.274


    gramgiven.delete("1.0",END)
    gramgiven.insert(END,store)

    poundgiven.delete("1.0",END)
    poundgiven.insert(END,store2)


    ouncegiven.delete("1.0",END)
    ouncegiven.insert(END,store3)


enterweight = Label(width=30,text="Enter Weight",font=("Arial",15))
enterweight.pack(padx=50,pady = 50)

enter = StringVar()

box = Entry(screen,width=30,textvariable =enter)
box.place(x = 150,y = 110)

gram = Label(width=20,text = "Grams (g)")
gram.place(x = 50,y =190)

pound = Label(width =20,text="Pounds(lbs)")
pound.place(x = 150, y = 190)

ounce = Label(width = 20,text = "Ounces (0z)")
ounce.place(x = 250,y =190)



gramgiven = Text(screen,height = 1, width = 10)
gramgiven.place(x = 80,y = 230)

poundgiven = Text(screen,height = 1,width = 10)
poundgiven.place(x = 190,y = 230)

ouncegiven = Text(screen,height = 1,width = 10)
ouncegiven.place(x= 300,y = 230)


convertbutton = Button(screen,width = 20,text="Convert",command=getweight)
convertbutton.place(x = 165,y = 150)






mainloop()