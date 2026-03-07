from tkinter import* 
from tkinter import messagebox
from random import randint 


screen = Tk()
screen.title("Guess the number")
screen.geometry("450x300")


number = randint(1,20)


def showmsgbox():
    name = entername.get()
    messagebox.showinfo("start game","ok "+name+" you look like you are worthy of this game. guess a number 1-20")


def check():
    guess = guessbox.get()
    guess = int(guess)

    if guess > number:
        messagebox.showinfo("was it right?","lower...")

    elif guess < number:
        messagebox.showinfo("was it right?","higher...")

    elif guess == number:
        messagebox.showinfo("was it right","YOOO TUFF U GOT IT RIGHT")




urname = Label(screen,text = "So uhh whats ur name?",font = ("Arial",10))
urname.place(x=50,y=50)

entername = Entry(screen,width = 30)
entername.place(x=50,y=80)


enternumber = Label(screen,text="whats the number then",font = ("Arial",10))
enternumber.place(x=50,y=150)


guessbox = Entry(screen,width=10)
guessbox.place(x=50,y=180)

ok = Button(screen,text = "alr heres my name",command =showmsgbox)
ok.place(x=250,y=70)



guessbutton = Button(screen,text="is this da number?",command = check)
guessbutton.place(x=150,y=180)








    


mainloop()