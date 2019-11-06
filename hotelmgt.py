from tkinter import *

############# create login window ######################

def loginwindow():
    mainheading()


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