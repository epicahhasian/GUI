from tkinter import* 

dsapp = Tk()
dsapp.title("Discount App")
dsapp.geometry("300x350")

def getdiscount():

    pricentry= float (enterprice.get())
    discountentry = float(enterdiscount.get())

    answer = pricentry* (discountentry/100)
    amounttext.delete(0,END)
    amounttext.insert(END,f"£{answer:.2f}")


    answer2= pricentry-answer 
    finaltext.delete(0,END)
    finaltext.insert(END,f"£{answer2:.2f}")




    
    

    



originalprice = Label (text = "Original Price (£):")
originalprice.place(x=10,y=25)
enterprice = Entry (width=30)
enterprice.place(x=110,y=25)




discount = Label (text="Discount(%):")
discount.place(x=30,y=55)
enterdiscount = Entry(width=30)
enterdiscount.place(x=110,y=55)


calculate = Button(bg="Green",text = "Calculate",command = getdiscount).place(x=100,y= 120)



amountsaved = Label(text="Amount Saved:")
amountsaved.place(x=10,y=190)
amounttext = Entry()
amounttext.place(x=110,y=190)


finalprice = Label(text="Final Price:")
finalprice.place(x = 30,y=220)
finaltext = Entry()
finaltext.place(x=110,y = 220)

mainloop()
