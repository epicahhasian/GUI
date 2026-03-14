from tkinter import* 

from tkinter.ttk import*


screen = Tk()
screen.title ("Times Tables")
screen.geometry("500x500")


mathtable = Label (screen,text = "Mathematical table:",font = ("Arial",10))
mathtable.place(x=160,y=50)

numberandrange = Label(screen,text = "Number and range:",font = ("Arial",10))
numberandrange.place(x=30,y=110)

num=IntVar()

tables = Combobox(screen,textvariable = num,width=5)
tables["values"] = tuple(range(101))
tables.place(x = 170,y = 110)


frequency1 = IntVar()

freq = Radiobutton(screen,text= "12",variable = frequency1,value =12)
freq.place(x=250,y= 110)

freq1 = Radiobutton (screen,text = "20",variable = frequency1, value = 20)
freq1.place(x=250,y=140)

freq2 = Radiobutton(screen,text ="30",variable = frequency1,value = 30)
freq2.place(x=250,y=170)

frequency1.set(12)




def showtable():
    table = ""
    for i in range(frequency1.get()+1):
        table += str(num.get())+"x"+str(i)+"="+str(num.get()*i)+"\n"
    tablesarenowshown.configure(text=table)

tablesarenowshown = Label(screen)
tablesarenowshown.place(x=400,y=0)

generate = Button(screen,text = "Generate Table",command = showtable)
generate.place(x=250,y=200)




mainloop()