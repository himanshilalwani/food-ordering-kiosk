from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector as connector
import pandas

def bill():
    def loaditemsincombo():
        mydb = connector.connect(host="localhost", user="root", password="root", database="food_chain")
        mycursor = mydb.cursor()
        mycursor.execute('select itemname from itemsmaster')
        result = mycursor.fetchall()
        DF = pandas.DataFrame(result, columns = ['itemname'])
        return list(DF['itemname'])

    def setselecteditem(event):
        txtselecteditem.delete(0, END)
        txtselecteditem.insert(0, itemscombo.get())
        mydb = connector.connect(host="localhost", user="root", password="root", database="food_chain")
        mycursor = mydb.cursor()
        mycursor.execute('select rate from itemsmaster where itemname="{}"'.format(txtselecteditem.get()))
        result = mycursor.fetchall()
        DF = pandas.DataFrame(result, columns = ['rate'])
        txtrate.delete(0, END)
        txtrate.insert(0, list(DF['rate']))

    def calculateamt():
        rate = txtrate.get()
        qty = qtyspin.get()
        if rate.isdigit() == False or qty.isdigit() == False:
            tkinter.messagebox.showinfo('Error', 'Invalid Entry, Try Again')
        else:
            amount = int(rate) * int(qty)
            txtamt.delete(0, END)
            txtamt.insert(0, amount)

    def additemtobill():
        txtdata.config(state = 'normal')
        item = txtselecteditem.get()
        rate = txtrate.get()
        qty = qtyspin.get()
        amount = txtamt.get()
        if (amount.isdigit() == False) or (int(amount) != (int(rate)*int(qty))) or qty == 0 or (qty.isdigit()==False) or (rate.isdigit() == False):
            tkinter.messagebox.showinfo('Error', 'Invalid Entry, Try Again')
        else:
            txtdata.insert(INSERT,item + '\t\t\t' + str(rate) + '\t\t' + str(qty) + '\t\t' + str(amount) + '\n\n')
            txtdata.config(state= 'disabled')
            global grandtotalint
            grandtotalint += int(txtamt.get())
            txtgrandtotal.delete(0, END)
            txtgrandtotal.insert(0, grandtotalint)

    def savebill():
        billdate = txtbilldate.get()
        name = txtname.get()
        if name.isspace() == True or name == '':
            tkinter.messagebox.showinfo('Error', 'Please enter your name')
        else:
            billdescription = txtdata.get(1.0, END)
            grandtotal = txtgrandtotal.get()
            mydb = connector.connect(host="localhost", user="root", password="root", database="food_chain")
            mycursor = mydb.cursor()
            q = 'insert into bill values({},"{}","{}","{}",{})'.format(c,billdate,name,billdescription,grandtotal)
            mycursor.execute(q)
            mydb.commit()
            tkinter.messagebox.showinfo("Information","Order Received!")
            mainwindow.destroy()

    mainwindow = Tk()
    mainwindow.title('Order Food')
    # mainwindow.configure(bg = "lightgrey")
    mainwindow.geometry('600x600')
    mainwindow.minsize(600,600)
    mainwindow.maxsize(600,600)

    heading = Label(mainwindow, text = "Generate Bill", font = "times 22 bold").place(x=220, y = 15)

    namelabel = Label(mainwindow, text = "Name", font = "times 14").place(x = 30, y = 70)
    txtname = Entry(mainwindow, width = 20)
    txtname.place(x = 80, y = 70)

    billdate = Label(mainwindow, text = "Date", font = "times 14").place(x = 300, y = 70 )
    txtbilldate = Entry(mainwindow, width = 20)
    txtbilldate.place(x = 340, y = 70)

    selectlabel = Label(mainwindow, text = "Item", font = "times 14").place(x=30, y=110)
    itemscombo = ttk.Combobox(mainwindow, width = 18, values = loaditemsincombo())
    itemscombo.place(x=80, y =110)
    itemscombo.current(0)
    itemscombo.bind('<<ComboboxSelected>>',setselecteditem)

    txtselecteditem = Entry(mainwindow, width = 25)
    txtselecteditem.place(x = 300, y=110)

    ratelabel = Label(mainwindow, text = "Rate", font = "times 14").place(x=30, y = 150)
    txtrate = Entry(mainwindow, width = 10)
    txtrate.place(x=80, y=150)

    qtylabel = Label(mainwindow, text = "Quantity", font = "times 14").place(x=200, y = 150)
    qtyspin = Spinbox(mainwindow, from_= 0, to = 50, width = 7)
    qtyspin.place(x=265, y =150 )

    amountlabel = Label(mainwindow, text = "Amount", font = "times 14").place(x=370, y = 150)
    txtamt = Entry(mainwindow, width = 10)
    txtamt.place(x=433, y = 150)

    btncalculate = Button(mainwindow, text = "Calculate", font = "times 14", width = 20, command = calculateamt)
    btncalculate.place(x=30, y = 195)
    btnadditems = Button(mainwindow, text = "Add Selected Item to Bill", font = "times 14", width = 41, command = additemtobill).place(x = 200, y = 195)

    txtdata = Text(mainwindow, width = 70, height = 18)
    txtdata.place(x = 30, y = 240)
    txtdata.insert(INSERT, "Item Name"+"\t\t\t"+"Rate"+"\t\t"+"Qty"+"\t\t"+"Amount"+"\n\n")
    txtdata.configure(state = "disabled")

    global grandtotalint
    grandtotalint = 0
    grandtotal = Label(mainwindow, text = "Grand Total", font = "times 14").place(x = 30, y = 500)
    txtgrandtotal = Entry(mainwindow, width = 10)
    txtgrandtotal.place(x = 115, y = 500)

    btnPlaceOrder = Button(mainwindow, text = "Place Your Order", font = "times 14", width = 30, command = savebill).place(x = 180, y = 550)

    #Showing current bill date
    mydb = connector.connect(host = "localhost", user = "root", password = "root", database = "food_chain")
    mycursor = mydb.cursor()
    mycursor.execute("select curdate()")
    result = mycursor.fetchall()
    DF = pandas.DataFrame(result, columns=['Date'])
    txtbilldate.insert(0,list(DF['Date']))

    a = "select * from bill"
    mycursor.execute(a)
    b = mycursor.fetchall()
    DF = pandas.DataFrame(b, columns=['billno','billdate','name','billdescription','grandtotal'])
    if DF.empty:
        c = 0
    else:
        c = max(DF['billno'])
    c += 1
    billno = Label(mainwindow, text = 'Bill No.: '+str(c), font = "times 14")
    billno.place(x = 30, y = 15)
    mydb.close()

    mainwindow.mainloop()