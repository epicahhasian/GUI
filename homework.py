from tkinter import* 
Top = Tk()

Top.title("Sign in")
Top.geometry("450x300")
Top.config (background = "Sky Blue")



username = Label(Top,text = "Username").place(x= 50,y=50)
password = Label(Top,text = "Password").place (x =50,y = 90)
entryboxusername = Entry(Top,width = 45).place (x= 130, y = 50)
entryboxpassword = Entry(Top,width = 45,show = "*").place (x= 130, y = 90)
Submitbutton = Button(Top, text = "Submit", width = 10, background ="Green").place (x = 90, y = 150)
Cancelbutton = Button(Top,text = "Cancel",width = 10, background = "Red", command = Top.destroy).place (x = 270, y = 150)
mainloop()

