from tkinter import *
import pymysql
from tkinter import messagebox



############### database conncetion #########################
def dbconfig():
    global mycursor,conn
    conn = pymysql.connect(host="localhost", user="root", db="wahtaz")
    mycursor = conn.cursor()

############## adminlogin ########################
def adminlogin():
    a=usernameVar.get()
    b=passwordVar.get()
    if a=="" or b=="":
        messagebox.showwarning("Login Check Window", "Please Enter User Name and Password")
        usernameVar.set("")
        passwordVar.set("")
    else:
        print(a,b)

############# create login window ######################

def loginwindow():
    #usernameVar.set("")
    #passwordVar.set("")
    loginLabel = Label(taz, text="Admin Login", font="Arial 30")
    loginLabel.grid(row=1, column=2, padx=(50, 0), columnspan=2, pady=10)

    usernameLabel = Label(taz, text="Username")
    usernameLabel.grid(row=2, column=2, padx=20, pady=5)

    passwordLabel = Label(taz, text="Password")
    passwordLabel.grid(row=3, column=2, padx=20, pady=5)

    global usernameVar
    usernameVar=StringVar()
    usernameEntry = Entry(taz, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=3, padx=20, pady=5)

    global passwordVar
    passwordVar = StringVar()
    passwordEntry = Entry(taz, show="*", textvariable=passwordVar)
    passwordEntry.grid(row=3, column=3, padx=20, pady=5)

    loginButton = Button(taz, text="Login", width=20, height=2, fg="green", bd=10, command=adminlogin)
    loginButton.grid(row=4, column=2, columnspan=2)





#############################################################
def mainheading():
    label = Label(taz, text="Hotel WahTaz Management system", bg="yellow", fg="green",
                  font=("Comic Sans Ms", 24, "bold"), padx=60)
    label.grid(row=0, columnspan=10)

taz=Tk()
mainheading()
loginwindow()

taz.geometry("900x600+120+50")
mainloop()