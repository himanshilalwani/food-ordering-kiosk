from tkinter import *
import tkinter.messagebox
import mysql.connector as connector
from tkinter.simpledialog import askstring

def checkpassword():
    pswd = askstring("Password", "Enter Password", show = "*")
    def save_create():
        mydb = connector.connect(host="localhost", user="root", password="root", database="food_chain")
        mycursor = mydb.cursor()
        global txtitemno, txtitemrate, txtitemname, createwindow
        itemno = txtitemno.get()
        itemname = txtitemname.get()
        itemrate = txtitemrate.get()
        if itemno.isdigit() == True and itemname.isspace() == False and itemname != '' and itemrate.isdigit() == True:
            qry = 'select exists(select * from itemsmaster where itemno = ({}))'.format(itemno)
            mycursor.execute(qry)
            bool_val = mycursor.fetchall()
            if bool_val[0][0] == 1:
                tkinter.messagebox.showinfo('Error', 'Item Number already exists')
            else:
                qry = "insert into itemsmaster values({},'{}',{})".format(itemno, itemname, itemrate)
                mycursor.execute(qry)
                mydb.commit()
                createwindow.destroy()
                tkinter.messagebox.showinfo("Information","Item Created Successfully!")
        else:
            tkinter.messagebox.showinfo("Error", "Invalid Entry")

    def create():
        global createwindow, mainwindow
        mainwindow.destroy()

        createwindow = Tk()
        createwindow.geometry("400x350")
        createwindow.title("Create Item")
        createwindow.minsize(400, 350)
        createwindow.maxsize(400, 350)

        heading = Label(createwindow, text = "Item Creation Form", font = 'times 16')
        heading.place(x=125, y = 40)

        itemnolbl = Label(createwindow, text = "Enter Item Number", font = "times 12")
        itemnolbl.place(x = 30, y= 100)
        global txtitemno
        txtitemno = Entry(createwindow)
        txtitemno.place(x = 150, y = 100)

        itemnamelbl = Label(createwindow, text = "Enter Item Name", font = "times 12")
        itemnamelbl.place(x = 30, y = 150)
        global txtitemname
        txtitemname = Entry(createwindow)
        txtitemname.place(x=150, y=150)

        itemratelbl = Label(createwindow, text = "Enter Item Rate", font = "times 12")
        itemratelbl.place(x=30, y = 200)
        global txtitemrate
        txtitemrate = Entry(createwindow)
        txtitemrate.place(x=150, y=200)

        Btnsave = Button(createwindow, text = "Save", font = "times 14", command = save_create)
        Btnsave.place(x=180, y=260)

    def save_mod():
        mydb = connector.connect(host="localhost", user="root", password="root", database="food_chain")
        mycursor = mydb.cursor()
        global txtno, txtmodname, txtmodrate, modifywindow
        modno = txtno.get()
        modname = txtmodname.get()
        modrate = txtmodrate.get()
        if modno.isdigit() == True and modname.isspace() == False and modname != '' and modrate.isdigit() == True:
            qry = 'select exists(select * from itemsmaster where itemno = ({}))'.format(modno)
            mycursor.execute(qry)
            bool_val = mycursor.fetchall()
            if bool_val[0][0] == 0:
                tkinter.messagebox.showinfo('Error', 'Item Does Not Exist')
            else:
                qry = "delete from itemsmaster where itemno = ({}) and itemname = ('{}')".format(modno, modname)
                mycursor.execute(qry)
                mydb.commit()
                qry =  'select exists(select * from itemsmaster where itemname = ("{}"))'.format(modname)
                mycursor.execute(qry)
                bool_val = mycursor.fetchall()
                if bool_val[0][0] == 1:
                    tkinter.messagebox.showinfo('Error', 'Duplicate Entry')
                else:
                    qry = "insert into itemsmaster values({},'{}',{})".format(modno, modname, modrate)
                    mycursor.execute(qry)
                    mydb.commit()
                    modifywindow.destroy()
                    tkinter.messagebox.showinfo("Information","Item Updated Successfully!")
        else:
            tkinter.messagebox.showinfo("Error", "Invalid Entry")



    def modify():
        global modifywindow, mainwindow
        mainwindow.destroy()

        modifywindow = Tk()
        modifywindow.geometry("400x350")
        modifywindow.title("Modify Item")
        modifywindow.minsize(400, 350)
        modifywindow.maxsize(400, 350)

        heading = Label(modifywindow, text="Item Modification Form", font='times 16')
        heading.place(x=125, y=40)

        nolbl = Label(modifywindow, text="Enter Item Number", font="times 12")
        nolbl.place(x=30, y=100)
        global txtno
        txtno = Entry(modifywindow)
        txtno.place(x=180, y=100)

        modnamelbl = Label(modifywindow, text="Enter Modified Item Name", font="times 12")
        modnamelbl.place(x=30, y=150)
        global txtmodname
        txtmodname = Entry(modifywindow)
        txtmodname.place(x=180, y=150)

        modratelbl = Label(modifywindow, text="Enter Modified Item Rate", font="times 12")
        modratelbl.place(x=30, y=200)
        global txtmodrate
        txtmodrate = Entry(modifywindow)
        txtmodrate.place(x=180, y=200)

        Btnsave = Button(modifywindow, text="Save", font="times 14", command=save_mod)
        Btnsave.place(x=180, y=260)

    def save_del():
        mydb = connector.connect(host="localhost", user="root", password="root", database="food_chain")
        mycursor = mydb.cursor()
        global txtdelno, txtdelname, delwindow
        delno = txtdelno.get()
        delname = txtdelname.get()
        if (delno.isdigit() == True) and (delname != '') and (delname.isspace() == False):
            qry = 'select exists(select * from itemsmaster where itemno = ({}) and itemname = ("{}"))'.format(delno, delname)
            mycursor.execute(qry)
            bool_val = mycursor.fetchall()
            if bool_val[0][0] == 0:
                tkinter.messagebox.showinfo('Error', 'Item Number and Item Name Do Not Match')
            else:
                qry = "delete from itemsmaster where itemno = ({}) and itemname = ('{}')".format(delno, delname)
                mycursor.execute(qry)
                mydb.commit()
                delwindow.destroy()
                tkinter.messagebox.showinfo("Information", "Item Deleted Successfully!")
        else:
            tkinter.messagebox.showinfo("Error", "Invalid Entry")

    def delete():
        global delwindow, mainwindow
        mainwindow.destroy()

        delwindow = Tk()
        delwindow.geometry("400x350")
        delwindow.title("Delete Item")
        delwindow.minsize(400, 350)
        delwindow.maxsize(400, 350)

        heading = Label(delwindow, text="Item Deletion Form", font='times 16')
        heading.place(x=125, y=40)

        lbldelno = Label(delwindow, text="Enter Item Number", font="times 12")
        lbldelno.place(x=30, y=110)
        global txtdelno
        txtdelno = Entry(delwindow)
        txtdelno.place(x=180, y=110)

        delnamelbl = Label(delwindow, text="Enter Item Name", font="times 12")
        delnamelbl.place(x=30, y=150)
        global txtdelname
        txtdelname = Entry(delwindow)
        txtdelname.place(x=180, y=150)

        Btnsave = Button(delwindow, text="Delete", font="times 14", command=save_del)
        Btnsave.place(x=180, y=260)

    if pswd == "1234":
        global mainwindow
        mainwindow = Tk()
        mainwindow.geometry("600x600")
        mainwindow.title("Admin")
        mainwindow.minsize(600,600)
        mainwindow.maxsize(600,600)

        createitem = Button(mainwindow, text = "Create Item", font = "times 20 bold", width = 20, command = create)
        createitem.place(x = 190, y = 150)
        modifyitem = Button(mainwindow, text="Modify Item", font="times 20 bold", width = 20, command = modify)
        modifyitem.place(x = 190, y = 250)
        deleteitem = Button(mainwindow, text="Delete Item", font="times 20 bold", width = 20, command = delete)
        deleteitem.place(x = 190, y = 350)