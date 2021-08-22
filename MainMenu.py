import tkinter
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image

import Manager
import ShowMenu
import Register
import OrderFood

#Main Window Geometry
mainWindow = Tk()
mainWindow.title("House of Doughnuts")
mainWindow.geometry("600x600")
mainWindow.maxsize(600,600)
mainWindow.minsize(600,600)

#Setting background image
backgroundImg = Image.open("bg-2.png")
# backgroundImg = backgroundImg.resize((600,600))
backgroundImg = ImageTk.PhotoImage(backgroundImg)
picture = Label(mainWindow, image = backgroundImg).place(x=0, y=0, relwidth = 1,relheight=1)

#Buttons over the background image

btnShowMenu = Button(mainWindow, text = "Show Menu", width =25, font = 'times 20 bold', command = ShowMenu.showMenu)
btnShowMenu.place(x=290, y =250)

btnOrderFood = Button(mainWindow, text = "Order Food", width =25, font = 'times 20 bold', command = OrderFood.bill)
btnOrderFood.place(x=290, y =310)

btnRegisterMember = Button(mainWindow, text = "Register Yourself", width =25, font = 'times 20 bold', command = Register.registerform)
btnRegisterMember.place(x=290, y =370)

btnExit = Button(mainWindow, text = "Exit", width =25, font = 'times 20 bold', command = mainWindow.destroy)
btnExit.place(x=290, y =430)

btnManager = Button(mainWindow, text = "Admin", width = 10, font = "times 16 bold", command = Manager.checkpassword)
btnManager.place(x=455, y=530)

mainWindow.mainloop()