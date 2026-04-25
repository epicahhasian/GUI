from tkinter import*
from tkinter.ttk import*
from tkinter import messagebox

screen = Tk()
screen.geometry ("500x200")

screen.title ("Pizza app")

name = Label (screen,text = "Welcome to Pizza Mansion, your order:")
name.place(x=150,y=0)

choice = Label(screen,text="Select type of pizza:")
choice.place(x=20,y=50)

quantity = Label(screen,text = "Quantity:")
quantity.place(x=20,y=100)



typeofpizza = StringVar()
pizza = Combobox(screen,textvariable = typeofpizza,width = 12)
pizza["values"]=("Pepperoni Pizza","Vegetabale Pizza","Vegan Pizza","Chicken Pizza","Cheese Pizza")
pizza.place (x=150,y=50)


num = IntVar()
numberofpizza = Combobox(screen,textvariable = num,width=12)
numberofpizza["values"]=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
numberofpizza.place(x=150,y=100)

size = StringVar()

small = Radiobutton(screen,text = "Small",variable = size, value="Small")
small.place(x= 400,y = 30 )

medium = Radiobutton(screen,text = "Medium",variable = size,value = "Medium")
medium.place(x=400,y=80)


large = Radiobutton(screen,text="Large",variable = size,value = "Large")
large.place(x=400,y=150)

size.set("Small")



def place():
    no = num.get()
    ty = typeofpizza.get()
    si = size.get()

    if not si:
        messagebox.showerror("Error:","Please select size of chosen pizza(s)")
        return 
    sizetext = {"Small":"Small","Medium":"Medium","Large":"Large"}
    result.config (text=f"You ordered {no} {ty} {si} size pizzas")





result = Label(screen,text = "")
result.place(x=180,y=180)






order = Button(screen,text="Order",command = place )
order.place(x=150,y=150)








mainloop()
