from tkinter import*

screen = Tk()
screen.title ("Listbox")
screen.geometry("450x300")


listbox = Listbox(screen, height = 45, width = 35, bg = "Maroon", fg = "Yellow")
fooditems = Label(screen,text = "Food Items")
listbox.insert(1,"Pizza")
listbox.insert(2,"Chicken")
listbox.insert(3,"Salad")
listbox.insert(4,"Burger")
listbox.insert(5,"Meatballs")


fooditems.pack()
listbox.pack()

mainloop()