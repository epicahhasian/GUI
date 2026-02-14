from tkinter import*

mirrorapp = Tk()

mirrorapp.title("Mirror App")
mirrorapp.geometry("450x300")

def textoutput():
    text = entervalue.get()
    copy.config(text = text)


entervalue = StringVar()
entertext = Entry(mirrorapp,width = 30,textvariable= entervalue)
entertext.pack(padx = 50, pady = 50)

copytext = Button(mirrorapp,text="Copy Text",command = textoutput)
copytext.pack(padx= 10, pady= 45)
copy= Label(mirrorapp, text = "")
copy.pack(padx = 10, pady = 10)
mainloop()