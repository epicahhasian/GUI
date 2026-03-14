from tkinter import*
from random import randint


screen = Tk()
screen.title ("Guess the number part 2 wowi")
screen.geometry ("350x300")

number = randint(1,10)


def checknumberlow():
    if number <=5:
       result.config (text = "well done bro u got it right")
    else:
       result.config(text = "nah u got it wrong the number was"+str(number))
       

def checknumberhigh():
    if number >5:
       result.config(text="well done bro u got it right")
    else:
       result.config(text = "nah u got it wrong the number was " +str(number))



    

    
     
      




comppicknumber= Label(screen,text = "Computer picked a number 1-10", font = ("Arial",15))
comppicknumber.place(x=40,y=0)


low = Button(screen,text = "Low (1-5)",bg = "Green",width=10,command = checknumberlow)
low.place(x=50,y=50)

high = Button(screen,text = "High (6-10)",bg = "Red",width = 10,command =  checknumberhigh)
high.place(x=200,y=50)

result = Label(screen,text = "",font = ("Arial",15))
result.place(x=10,y=100)

mainloop()