from tkinter import*

frame = Tk()

frame.geometry("450x300")

chocolate = Frame(frame)
chocolate.pack()

cake = Frame(frame)
cake.pack(side=BOTTOM)

chocolatebutton1 = Button(chocolate, text="Chocolate", bg = "Brown", fg = "Yellow")
chocolatebutton1.pack(side = TOP)

chocolatebutton2 = Button(chocolate,text = "Dark Chocolate", bg = "Black",fg = "Yellow")
chocolatebutton2.pack(side = TOP)

chocolatebutton3 = Button (chocolate, text = "White Chocolate", bg = "Grey",fg = "Yellow")
chocolatebutton3.pack (side = TOP)


cakebutton1 = Button (cake, text = "Coffee Cake", bg = "Gold",fg = "Black" )
cakebutton1.pack(side = TOP)

cakebutton2 = Button (cake,text = " Strawberry Cake", bg = "Red", fg = "White")
cakebutton2.pack(side = TOP)

cakebutton3 = Button(cake, text = "Carrot Cake", bg = "Orange",fg = "Black")
cakebutton3.pack(side = TOP)



mainloop()