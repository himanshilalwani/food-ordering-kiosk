from tkinter import *
import mysql.connector as connector
import pandas
from PIL import Image, ImageTk

def showMenu():
    window = Tk()
    window.title('Menu')
    window.geometry("600x600")
    window.maxsize(600, 600)
    window.minsize(600, 600)

    mydb = connector.connect(host = 'localhost', user = 'root', passwd = "root", database = 'food_chain')
    mycursor = mydb.cursor()
    mycursor.execute('select itemname, rate from itemsmaster;')
    itemname = mycursor.fetchall()
    DF = pandas.DataFrame(itemname, columns=["Itemname","Rate"])

    heading = Label(window, text = "MENU", font = 'times 25 bold')
    heading.place(x = 250, y = 20)

    text = Text(window, width = 600, height = 24, font = 'times 15 bold')
    text.place(x = 0, y = 70)
    text.insert(INSERT,"\t\t            Item\t\t\t          Rate\n\n")
    for ri,rd in DF.iterrows():
        a = DF.loc[ri, "Itemname"]
        b = DF.loc[ri, "Rate"]
        text.insert(INSERT, '\t\t   ')
        text.insert(INSERT, a)
        text.insert(INSERT, '\t\t\t           ')
        text.insert(INSERT, b)
        text.insert(INSERT, '\n\n')
    text.configure(state="disabled")

    btnBack= Button(window, text="Back", width=10, font="times 16 bold", command = window.destroy)
    btnBack.place(x=455, y=530)

    window.mainloop()
