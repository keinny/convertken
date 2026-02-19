from tkinter import *

class CurrencyConverter:
    def __init__(self):
        window = Tk()
        window.title("CurrencyConverter")
        window.configure(bg="green")
        Label(window,font="Helvetica 12 bold", bg="yellow", text="Amout to convert").grid(row=1, column=1,sticky=W)
        Label(window,font="Helvetica 12 bold", bg="yellow", text="conversion Rate").grid(row=2, column=1,sticky=W)
        Label(window,font="Helvetica 12 bold", bg="yellow", text="converted Amount").grid(row=3, column=1,sticky=W)
        self.amounttoConvertVar = StringVar()
        Entry(window, textvariable= self.amounttoConvertVar, justify=RIGHT).grid(row=1,column=2)
        self.conversionRateVar = StringVar()
        Entry(window, textvariable= self.conversionRateVar, justify= RIGHT).grid(row=2,column=2)
        self.convertdAmountVar = StringVar()
        lblConvertedAmount = Label(window,font="Helvetica 12 bold", bg="yellow", textvariable=self.convertdAmountVar).grid(row=3,column=2,sticky = E)

        #creating button

        btConvertedAmount = Button(window, text="Convert",font="Helvetica 12 bold", bg="blue", fg="white", command=self.ConvertedAmount).grid(row=4,column=2,sticky=E)
        btConvertedwewqewqeAmount = Button(window, text="Convert",font="Helvetica 12 bold", bg="red", fg="white", command=self.ConvertedAmount).grid(row=4,column=3,sticky=E)

        window.mainloop()