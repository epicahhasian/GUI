from tkinter import* 

Top =Tk()

Top.title ("Log in")
Top.geometry("400x350")
Top.config(background = "Red")

#label 
username = Label(Top,text="Username").place(x =50,y = 50)
password = Label(Top,text="Password").place(x=50,y=90)
entryboxpassword = Entry(Top, width = 45, show="*").place (x = 120,y = 90)
entryboxusername = Entry(Top,width = 45).place (x= 120, y = 50)
submitbutton = Button(Top,text = "Submit").place (x =50,y = 150)
Top.mainloop()