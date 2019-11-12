from tkinter import *
from tkinter import messagebox,ttk,filedialog
from tkinter import ttk
import pymysql
from  datetime import datetime
from tkinter.ttk import Combobox
taz=Tk()

# ========mainTreeView======================
tazTV = ttk.Treeview(height=10, columns=('Item Name''Rate','Type'))
tazTV1 = ttk.Treeview(height=10, columns=('Item Name''Rate', 'Type', 'aa','as'))
############### database conncetion #########################
def dbconfig():
    global mycursor,conn
    conn = pymysql.connect(host="localhost", user="root", db="wahtaz")
    mycursor = conn.cursor()

#########################remove all widgets from screen #################

def remove_all_widgets():
    global taz
    for widget in taz.winfo_children():
        widget.grid_remove()
#############################################################
def mainheading():
    label = Label(taz, text="Hotel WahTaz Management system", bg="yellow", fg="green",
                  font=("Comic Sans Ms", 40, "bold"), padx=62, pady=0)
    label.grid(row=0, columnspan=4)





############  login action ##################
def adminlogin():
    dbconfig()
    username=usernameVar.get()
    password=passwordVar.get()
    que="select * from user_info where userid=%s and password=%s"
    val=(username,password)
    mycursor.execute(que,val)
    data = mycursor.fetchall()
    flag = False
    for row in data:
        flag = True

    conn.close()
    if flag == True:
        welcomewindow()

    else:
        messagebox.showerror("Invalid User Credential",'either User Name or Password is incorrect')
        usernameVar.set("")
        passwordVar.set("")
############# validation ######################
def only_numeric_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False

def only_char_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isalpha() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False
callback = taz.register(only_char_input)  # registers a Tcl to Python callback
callback1 = taz.register(only_numeric_input)  # registers a Tcl to Python callback
############# def logout ########################
def logout():
    remove_all_widgets()
    mainheading()
    loginwindow()
############## back buttton #####################

def backbutton():
    remove_all_widgets()
    mainheading()
    welcomewindow()
################ ondouble click get data ##############
def OnDoubleClick(event):
    item = tazTV.selection()
    itemNameVar1 = tazTV.item(item, "text")
    item_detail = tazTV.item(item, "values")

    itemnameVar.set(itemNameVar1)
    itemrateVar.set(item_detail[0])
    itemTypeVar.set(item_detail[1])
##########update item #####################
def updateItem():
    name = itemnameVar.get()
    rate = itemrateVar.get()
    type = itemTypeVar.get()
    dbconfig()
    query="update itemlist set item_rate=%s,item_type=%s where item_name=%s"
    val=(rate,type,name)
    mycursor.execute(query,val)
    conn.commit()
    messagebox.showinfo("Update Data", 'Item Updated Successfully')
    itemnameVar.set("")
    itemrateVar.set("")
    itemTypeVar.set("")
    getItemInTreeView()


##########delete item #####################
def deleteItem():
    name = itemnameVar.get()
    rate = itemrateVar.get()
    type = itemTypeVar.get()
    dbconfig()
    query = "delete from itemlist where item_name=%s"
    val = (name)
    mycursor.execute(query, val)
    result=messagebox.askyesno("Delete Dialog box","Do you want to Delete this Item")
    if result == True:
        conn.commit()
        messagebox.showinfo("Delete Data", 'Item Deleted Successfully')
    else:
        pass
    itemnameVar.set("")
    itemrateVar.set("")
    itemTypeVar.set("")
    getItemInTreeView()


############ get Item in tree view ###############
def getItemInTreeView():
    # to delete already inserted item
    records = tazTV.get_children()

    for element in records:
        tazTV.delete(element)

    # insert data in treeview
    conn = pymysql.connect(host="localhost", user="root", db="wahtaz")
    mycursor = conn.cursor(pymysql.cursors.DictCursor)
    print(mycursor)
    query = "select * from itemlist"
    mycursor.execute(query)
    data = mycursor.fetchall()
    print(data)
    for row in data:
        tazTV.insert('', 'end', text=row['item_name'], values=(row["item_rate"], row["item_type"]))
    conn.close()
    tazTV.bind("<Double-1>", OnDoubleClick)
############### get combo value ################
'''def comboget():
    return (itemType.get())'''

################# add item into database#########################
def additem():
    additemwindow()
    name=itemnameVar.get()
    rate=itemrateVar.get()
    type=itemTypeVar.get()
    print(name,rate,type)
    dbconfig()
    query = "insert into itemlist (item_name,item_rate,item_type) values(%s,%s,%s);"
    val = (name,rate,type)
    mycursor.execute(query,val)
    conn.commit()
    messagebox.showinfo("Save Data", 'Item Inserted Successfully')
    itemnameVar.set("")
    itemrateVar.set("")
    itemTypeVar.set("")
    getItemInTreeView()


################## add item window ##################
itemnameVar=StringVar()
itemrateVar=StringVar()
itemTypeVar=StringVar()

def additemwindow():
    remove_all_widgets()
    mainheading()

    itemnameLabel = Label(taz, text="ITEM DETAILS", font="Arial 30")
    itemnameLabel.grid(row=1, column=2, padx=(50, 0), columnspan=1, pady=10)

    ###############################
    billButton = Button(taz, text="Back", width=20, height=2, fg="green", bd=10, command=backbutton)
    billButton.grid(row=1, column=0, columnspan=1)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=logout)
    logoutButton.grid(row=3, column=0, columnspan=1)

    ###########################

    itemnameLabel = Label(taz, text="Item name")
    itemnameLabel.grid(row=2, column=1, padx=20,  pady=5)


    itemrateLabel = Label(taz, text="Item Rate")
    itemrateLabel.grid(row=3, column=1, padx=20, pady=5)

    itemTypeLabel = Label(taz, text="Item Type")
    itemTypeLabel.grid(row=4, column=1, padx=20, pady=5)

    itemnameEntry = Entry(taz, textvariable=itemnameVar)
    itemnameEntry.grid(row=2, column=2, padx=20, pady=5)
    itemnameEntry.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation

    itemrateEntry = Entry(taz, textvariable=itemrateVar)
    itemrateEntry.grid(row=3, column=2, padx=20, pady=5)
    itemrateEntry.configure(validate="key", validatecommand=(callback1, "%P"))  # enables validation

    itemTypeEntry = Entry(taz, textvariable=itemTypeVar)
    itemTypeEntry.grid(row=4, column=2, padx=20, pady=5)
    itemTypeEntry.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation
    '''global itemType
    #l = ["BreakFast", "Lunch", "Dinner"]
    itemType = Combobox(taz, values=l, height=2)
    itemType.set("Select Item type")
    itemType.grid(row=4, column=3, padx=20, pady=5)'''

    label = Label(taz)
    label.grid(row=5, column=2, padx=20, pady=5)

    additemButton = Button(taz, text="Add Item", width=20, height=2, fg="green", bd=10,command=additem)
    additemButton.grid(row=3, column=3, columnspan=1)

    updateButton = Button(taz, text="UpDate Item", width=20, height=2, fg="green", bd=10, command=updateItem)
    updateButton.grid(row=1, column=3, columnspan=1)

    deleteButton = Button(taz, text="Delete Item", width=20, height=2, fg="green", bd=10,command=deleteItem)
    deleteButton.grid(row=6, column=3, columnspan=1)

    ###############################################
    tazTV.grid(row=7, column=0, columnspan=3)
    style=ttk.Style(taz)
    style.theme_use('clam')
    style.configure("Treeview",fieldbackground="green")
    scrollBar = Scrollbar(taz, orient="vertical", command=tazTV.yview)
    scrollBar.grid(row=7, column=2, sticky="NSE")

    tazTV.configure(yscrollcommand=scrollBar.set)

    tazTV.heading('#0', text="Item Name")
    tazTV.heading('#1', text="Rate")
    tazTV.heading('#2', text="Type")

    getItemInTreeView()

########## option call back #################

def OptionCallBack(*args):
    global itemname
    itemname=combovariable.get()
    #print(itemname)
    aa=ratelist()
    #print(aa)
    baserate.set(aa)
    global v
    for i in aa:
        for j in i:
           v  = j



def OptionCallBack1(*args):
    global qty
    qty=qtyvariable.get()
    #cost.set(int('0'))
    finalvalue = int(v) * int(qty)
    cost.set(finalvalue)
################
def ratelist():
    dbconfig()
    que="select item_rate from itemlist where item_name=%s"
    val=(itemname)
    mycursor.execute(que,val)

    data = mycursor.fetchall()
    #print(data)
    return data
######## get data in combo box ###############

def combo_input():
    dbconfig()

    mycursor.execute('SELECT item_name FROM itemlist')

    data = []

    for row in mycursor.fetchall():
        data.append(row[0])

    return data
###########date time solution ##########
global x
x=datetime.now()

######### bill generation window #################

datetimeVar=StringVar()
datetimeVar.set(x)
customerNameVar=StringVar()
mobileVar=StringVar()
combovariable=StringVar()
baserate=StringVar()
qtyvariable=StringVar()
cost=StringVar()
def billgenerationwindow():
    remove_all_widgets()
    mainheading()

    itemnameLabel = Label(taz, text="BILL DETAILS", font="Arial 30")
    itemnameLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)

    billButton = Button(taz, text="Back", width=20, height=2, fg="green", bd=10, command=backbutton)
    billButton.grid(row=1, column=0, columnspan=1)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=logout)
    logoutButton.grid(row=5, column=0, columnspan=1)

    ##############################################
    dateTimeLabel = Label(taz, text="Date/Time")
    dateTimeLabel.grid(row=2, column=2, padx=20, pady=5)

    dateTimeEntry = Entry(taz, textvariable=datetimeVar)
    dateTimeEntry.grid(row=2, column=3, padx=20, pady=5)


    customerNameLabel = Label(taz, text="Customer Name")
    customerNameLabel.grid(row=3, column=2, padx=20, pady=5)

    customerNameEntry = Entry(taz, textvariable=customerNameVar)
    customerNameEntry.grid(row=3, column=3, padx=20, pady=5)
    customerNameEntry.configure(validate="key", validatecommand=(callback, "%P"))  # enabl


    mobileLabel = Label(taz, text="Contact No")
    mobileLabel.grid(row=4, column=2, padx=20, pady=5)

    mobileEntry = Entry(taz, textvariable=mobileVar)
    mobileEntry.grid(row=4, column=3, padx=20, pady=5)
    mobileEntry.configure(validate="key", validatecommand=(callback1, "%P"))  # enables

    selectLabel = Label(taz, text="Select Item")
    selectLabel.grid(row=5, column=2, padx=20, pady=5)

    l=combo_input()

    c = ttk.Combobox(taz, values=l, textvariable=combovariable)
    c.set("Select Item")
    combovariable.trace('w', OptionCallBack)
    c.grid(row=5, column=3, padx=20, pady=5)
    ##########################################

    rateLabel = Label(taz, text="Rate ")
    rateLabel.grid(row=6, column=2, padx=20, pady=5)

    rateEntry = Entry(taz, textvariable=baserate)
    rateEntry.grid(row=6, column=3, padx=20, pady=5)

    quantityLabel = Label(taz, text="Quantity ")
    quantityLabel.grid(row=7, column=2, padx=20, pady=5)

    global qtyvariable
    qtyvariable = IntVar()
    l2 = [1, 2, 3, 4, 5]
    qty = ttk.Combobox(taz, values=l2, textvariable=qtyvariable)
    qty.set("Select Quantity")
    qtyvariable.trace('w', OptionCallBack1)
    qty.grid(row=7, column=3, padx=20, pady=5)

    costLabel = Label(taz, text="Cost ")
    costLabel.grid(row=8, column=2, padx=20, pady=5)
    costEntry = Entry(taz, textvariable=cost)
    costEntry.grid(row=8, column=3, padx=20, pady=5)

    billButton = Button(taz, text="Bill Generation", width=20, height=2, fg="green", bd=10,
                        command=bill)
    billButton.grid(row=9, column=2, columnspan=2)

    printbillButton = Button(taz, text="Print Bill", width=20, height=2, fg="green", bd=10,
                        command=printbill)
    printbillButton.grid(row=9, column=0, columnspan=1)


################ bill generation ###################

def bill():
    dt=datetimeVar.get()
    custname = customerNameVar.get()
    mobile=mobileVar.get()
    item_name=itemname
    itemrate = v
    itemqty= qtyvariable.get()
    total=cost.get()
    print(dt,custname,mobile,item_name,itemrate,itemqty,total)
    dbconfig()

    query = "insert into bill (datetime,customer_name,contact_no,item_name,item_rate,item_qty,cost) values(%s,%s,%s,%s,%s,%s,%s);"
    val = (dt,custname,mobile,item_name,itemrate,itemqty,total)
    mycursor.execute(query, val)
    conn.commit()
    messagebox.showinfo("Save Data", 'Bill Generated Successfully')
    customerNameVar.set("")
    mobileVar.set("")

    itemrateVar.set("")
    cost.set("")
    remove_all_widgets()
    billgenerationwindow()

def printbill():
    finallybill()
############ finally bill #####


def finallybill():
    remove_all_widgets()
    mainheading()
    itemnameLabel = Label(taz, text="BILL DETAILS", font="Arial 30")
    itemnameLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)

    billButton = Button(taz, text="Back", width=20, height=2, fg="green", bd=10, command=backbutton)
    billButton.grid(row=1, column=0, columnspan=1)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=logout)
    logoutButton.grid(row=1, column=3, columnspan=1)



    back_btnBill = Button(taz, text="Double Click Data to Print Reciept", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                          ).grid(row=2, column=1, columnspan=2, padx=20, pady=5)

    #displayDB.configure(yscrollcommand=scrollBar.set)

    tazTV1.grid(row=3, column=0,columnspan=8)
    scrollBar = Scrollbar(taz, orient="vertical", command=tazTV1.yview)
    scrollBar.grid(row=3, column=8, sticky="NSE")
    tazTV1.heading('#0', text="Date/Time")
    tazTV1.heading('#1', text="Name")
    tazTV1.heading('#2', text="Mobile")
    tazTV1.heading('#3', text="Selected Food")
    '''tazTV1.heading('#4', text="Rate")
    tazTV1.heading('#5', text="Quantity")'''
    tazTV1.heading('#4', text="Total Amount")
    displayBill()

################ ondouble click get data ##############
def OnDoubleClick2(event):
    item = tazTV1.selection()
    global itemNameVar11
    itemNameVar11 = tazTV1.item(item, "text")
    item_detail1 = tazTV1.item(item, "values")
    #print(item)
    #print(itemNameVar11)
    #print(item_detail1)
    reciept()

###############display bill ############
##################################################### Updating The CUstomer Bill##########################
def displayBill():
    # fetch all data into records
    dbrecords=tazTV1.get_children()
    # to delete all the records from tree view which is already exist
    for element in dbrecords:
        tazTV1.delete(element)

    # to load the table data to tree view

    conn = pymysql.connect(host="localhost", user="root", db="wahtaz")

    mycursor = conn.cursor(pymysql.cursors.DictCursor)

    query="select * from bill "
    mycursor.execute(query)
    data=mycursor.fetchall()
    #print(data)
    for row in data:
        tazTV1.insert('', 'end', text=row['datetime'], values=(row["customer_name"], row["contact_no"],row["item_name"],row["cost"]))

    conn.close()
    tazTV1.bind("<Double-1>", OnDoubleClick2)
########### print reciept ############################

def reciept():
    global itemLists
    global totalCost

    billString = ""
    billString += "=====================Receipt==========================\n\n"
    billString += "===================Customer Detail====================\n"


    conn = pymysql.connect(host="localhost", user="root", passwd="", db="wahtaz")
    cursor = conn.cursor()

    query = "select * from bill WHERE datetime='{}';".format(itemNameVar11)
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)

    for row in data:
        #billString.insert('', 'end', text=row['TimeAndDate'], values=(row["Name"], row["Mobile"],row["FoodName"], row["Rate"], row["Quantity"], row["TotalAmount"]))
        '''print("Time and date = ",row[1])
        print("Name = ",row[2])
        print("Mobile = ",row[3])
        print("Food Name = ",row[4])
        print("Rate = ",row[5])
        print("Quantity=",row[6])
        print("Total Cost=", row[7])'''
        billString += "{}{:<20}{:<10}\n".format("Date/Time","", row[1])
        billString += "{}{:<20}{:<10}\n".format("Customer Name", "",row[2])
        billString += "{}{:<20} {:<10}\n".format("Contact No","", row[3])
        billString += "\n====================Item Detail=====================\n"
        billString += "{:<10}{:<10}{:<15}{:15}".format("Item Name", "Rate", "Quantity","Total cost")
        billString += "\n{:<10}{:<10}{:<25}{:25}\n".format(row[4], row[5], row[6],row[7])
        billString += "\n=====================================================\n"


        billString += "{}{:<10}{:<15}{:<10}\n".format("Total Cost", " ", " ", row[7])
        billString += "\n============Thanks Please Visit Again===============\n"

    billFile = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if billFile is None:
        messagebox.showerror("Invalid file Name", "Please enter valid name")
    else:
        billFile.write(billString)
        billFile.close()

    #print(billString)

    itemLists = []
    totalCost = 0.0
###################################################
usernameVar = StringVar()
passwordVar = StringVar()

def loginwindow():
    usernameVar.set("")
    passwordVar.set("")
    loginLabel = Label(taz, text="Admin Login", font="Arial 30")
    loginLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)

    usernameLabel = Label(taz, text="Username")
    usernameLabel.grid(row=2, column=1, padx=20, pady=5)

    passwordLabel = Label(taz, text="Password")
    passwordLabel.grid(row=3, column=1, padx=20, pady=5)

    usernameEntry = Entry(taz, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=2, padx=20, pady=5)
    usernameEntry.configure(validate="key", validatecommand=(callback, "%P"))

    passwordEntry = Entry(taz, show="*", textvariable=passwordVar)
    passwordEntry.grid(row=3, column=2, padx=20, pady=5)

    loginButton = Button(taz, text="Login", width=20, height=2, fg="green", bd=10, command=adminlogin)
    loginButton.grid(row=4, column=1, columnspan=2)

########## Welcome Window#######################
def welcomewindow():
    remove_all_widgets()
    mainheading()
    welcomeLabel = Label(taz, text="Welcome User", font="Arial 30")
    welcomeLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)

    additemButton = Button(taz, text="Manage Restaurant", width=20, height=2, fg="green", bd=10, command=additemwindow)
    additemButton.grid(row=3, column=0, columnspan=1)

    billButton = Button(taz, text="Bill Generation", width=20, height=2, fg="green", bd=10, command=billgenerationwindow)
    billButton.grid(row=3, column=1, columnspan=2)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=logout)
    logoutButton.grid(row=3, column=3, columnspan=1)

###############################################

taz.title("Hotel WAhTaz Managment System")
mainheading()
loginwindow()

taz.geometry("1055x670+120+00")
#taz.resizable(0,0)
mainloop()