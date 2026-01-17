from tkinter import*
from tkinter.ttk import*

Top = Tk()

Top.title("Menu")
Top.geometry("450x300")

Menubar = Menu(Top)
File = Menu(Menubar,tearoff = 0)
Menubar.add_cascade(label = "File",menu = File)
File.add_command(label = "Newfile", command = None)
File.add_command(label = "OpenFile",command = None)
File.add_command(label = "Save", command = None)
File.add_separator()
File.add_command(label = "Exit", command = Top.destroy)



Edit = Menu(Menubar,tearoff = 0)
Menubar.add_cascade(label = "Edit",menu = Edit)
Edit.add_command(label = "Undo",command = None)
Edit.add_command(label = "Redo",command = None)
Edit.add_command(label = "Copy",command = None)
Edit.add_command (label = "Paste",command = None)

View = Menu(Menubar, tearoff = 0)
Menubar.add_cascade(label = "View",menu = View)
View.add_command(label = "Open View",command = None)
View.add_command(label = "Search",command = None)
View.add_command(label = "Run",command = None)
View.add_separator()
View.add_command(label = "DebugConsole",command = None)

Top.config(menu = Menubar)
mainloop()


