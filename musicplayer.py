from tkinter import* 
screen= Tk()
screen.geometry("450x300")
screen.title("Playlist")

musicplayer = Listbox(screen,width= 35, height=10)

playlist = Label (screen,text= "My Playlist")


musicplayer.insert(1,"1. Montagem Rugada")
musicplayer.insert(2,"2. Montagem Rebola")
musicplayer.insert(3,"3. Montagem Batida")
musicplayer.insert(4, "4. NO BATIDAO")
musicplayer.insert(5,"5. VAI VAI TRAIR")
musicplayer.insert(6,"6. Voce ne mira")
musicplayer.insert(7,"7. LUA NA PRACA")
musicplayer.insert(8,"8. LOUCURA LETAL")
musicplayer.insert(9,"9. Reinado")
musicplayer.insert(10,"10. ECHAME")




Play = Button(screen,text="Play",bg = "Green").place (x = 130, y = 200)
Pause = Button(screen,text = "Pause", bg = "Orange").place (x = 200, y = 200)
Next = Button (screen,text = "Next", bg = "Sky Blue").place (x = 270, y = 200)



playlist.pack()
musicplayer.pack()






mainloop()


