from tkinter import *
import tkinter.messagebox
import mysql.connector as connector

def registerform():
    def newmember():
        mydb = connector.connect(host = 'localhost', user = 'root', password = 'root', database = 'food_chain')
        mycursor = mydb.cursor()

        firstname = txtfirstname.get()
        lastname = txtlastname.get()
        address = txtaddress.get()
        mobile = txtmobile.get()

        if firstname == '' or lastname == '' or address == '' or mobile == '':
            tkinter.messagebox.showinfo('Error', 'Enter the relevant details')
        elif len(mobile)!=10 or mobile[0] == '-' or mobile[0] == '0':
            tkinter.messagebox.showinfo('Error', 'Invalid mobile number')
        else:
            qry = 'select exists(select * from memberdetails where mobile = ("{}"))'.format(mobile)
            mycursor.execute(qry)
            bool_val = mycursor.fetchall()
            if bool_val[0][0] == 1:
                tkinter.messagebox.showinfo('Error', 'Mobile number already registered')
                mainwindow.destroy()
            else:
                qry = "insert into memberdetails values('{}','{}',{},'{}')".format(firstname,lastname,mobile, address)
                mycursor.execute(qry)
                mydb.commit()
                mainwindow.destroy()
                tkinter.messagebox.showinfo('Information','Registered Successfully')

    mainwindow = Tk()
    mainwindow.geometry('600x600')
    mainwindow.minsize(600,600)
    mainwindow.maxsize(600,600)
    mainwindow.title('Register')


    lblregister = Label(mainwindow, text = "Register Yourself for Amazing Offers", font = 'times 23 bold').place(x = 100, y = 70)
    lblfirstname = Label(mainwindow, text = "Enter your first name", font = "times 18").place(x = 60, y = 160)
    lbllastname = Label(mainwindow, text="Enter your last name", font="times 18").place(x=60, y=220)
    lbladdress = Label(mainwindow, text="Enter your address", font="times 18").place(x=60, y=280)
    lblmobile = Label(mainwindow, text="Enter your mobile number", font="times 18").place(x=60, y=340)

    txtfirstname = Entry(mainwindow)
    txtfirstname.place(x=310, y=160)
    txtlastname = Entry(mainwindow)
    txtlastname.place(x=310, y=220)
    txtaddress = Entry(mainwindow)
    txtaddress.place(x=310, y=280)
    txtmobile = Entry(mainwindow)
    txtmobile.place(x=310, y=340)

    Btnsave = Button(mainwindow, text = "Save", font = "times 18", width = 10, command = newmember)
    Btnsave.place(x=230, y =450)

    mainwindow.mainloop()

