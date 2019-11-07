from tkinter import *
import pymysql
from tkinter import messagebox

############ to clear all widgets on the screen #################
def remove_all_widgets():
    global taz
    for widget in taz.winfo_children():
        widget.grid_remove()

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
        dbconfig()
        que = "select * from user_info where userid=%s and password=%s"
        val = (a,b)
        mycursor.execute(que, val)
        flag = False
        data = mycursor.fetchall()
        for row in data:
            flag = True

        conn.close()
        if flag == True:
            welcomewindow()

        else:
            messagebox.showerror("Invalid User Credential", 'either User Name or Password is incorrect')
            usernameVar.set("")
            passwordVar.set("")


############# create wlcome window ######################

def welcomewindow():
    remove_all_widgets();
    mainheading()
    loginLabel = Label(taz, text="Welcome User", font="Arial 30")
    loginLabel.grid(row=1, column=2, padx=(50, 0), columnspan=5, pady=10)


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