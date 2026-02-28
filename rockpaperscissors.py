from tkinter import*
import random 

screen = Tk()
screen.title("Rock Paper Scissors")
screen.geometry("600x400")

titl= Label(screen,text = "Rock Paper Scissors",font=("Arial",20))
titl.place(x = 170,y =20)

playerscore = 0
botscore = 0 

options = [("Rock",0),("Paper",1),("Scissors",2)]


def botwinner():
    global playerscore,botscore 
    botscore+=1
    whowins.config(text="Bot wins :(")
    botwins.config(text="Bot wins: "+str(botscore))
    yourwins.config(text="Your wins:"+str(playerscore))



def playerwinner():
    global playerscore,botscore
    playerscore +=1
    whowins.config(text="You win :D")
    botwins.config(text="Bot wins: "+str(botscore))
    yourwins.config(text="Your wins:"+str(playerscore))



def tie():
    global playerscore,botscore
    whowins.config(text="Tie")
    botwins.config(text="Bot wins: "+str(botscore))
    yourwins.config(text="Your wins:"+str(playerscore))


def botchoice():
    return random.choice(options)


def playerchoice(playerinput):
    global playerscore,botscore
    print(playerinput)
    botinput = botchoice()
    print(botinput)
    youselected.config(text = "You Selected:"+playerinput[0])
    botselected.config(text = "Bot Selected:"+botinput[0])
    if playerinput==botinput:
        tie()

    if playerinput == 0:
        if botinput== 1:
            botwinner()
        elif botinput==2:
            playerwinner()

    if playerinput== 1:
        if botinput==0:
            playerwinner()
        elif botinput==2:
            botwinner()

    if playerinput==2:
        if botinput==0:
            botwinner()
        elif botinput==1:
            playerwinner()
    
    



    


whowins = Label(screen,text="Let's start the game...",font=("Arial",15))
whowins.place(x=200,y=70)
youroptions = Label(screen,text="Your options:",font=("Arial",15))
youroptions.place(x=30,y=120)

rock = Button(screen,text="Rock",bg ="Pink",width=15,font=("Arial",10),command=lambda:playerchoice(options[0]))
rock.place(x=50,y=170)

paper = Button(screen,text = "Paper",bg = "Yellow",width = 15,font = ("Arial",10),command = lambda:playerchoice(options[1]))
paper.place(x = 210, y = 170)

scissors = Button(screen,text = "Scissors",bg = "Red",width = 15,font = ("Arial",10),command=lambda:playerchoice(options[2]))
scissors.place (x = 370,y=170)



score = Label(screen,text = "Score:",font=("Arial",15))
score.place(x=30,y=240)


youselected = Label(screen,text="You selected:",font=("Arial",12))
youselected.place(x=50,y=280)

botselected = Label(screen,text="Bot selected:",font=("Arial",12))
botselected.place(x=50,y=350)

yourwins = Label(screen,text= "Your wins:",font = ("Arial",12))
yourwins.place(x= 300,y=280)


botwins = Label(screen,text="Bot wins:",font = ("Arial",12))
botwins.place(x=300,y = 350)







mainloop()