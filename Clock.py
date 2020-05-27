'''
@auteur : walid.menghour
@date : 20/05/2020
@version: 1.00
'''
from tkinter import *
from tkinter import ttk
from tkinter import font
import datetime

#Define Function for exit() {I can using exit()}
def quit(*args):
    root.destory()

#Define fun for chainge the time in the widget 
def clock_time():
    time = datetime.datetime.now()
    time = (time.strftime("%H:%M:%S"))                     #is the format of time [Hours:Minutes:Secondes]
    txt.set(time)                                          #chainge the time
    root.after(1000, clock_time)                           #after 1000ms Chaine the time


root = Tk()                                                #define the object

root.title("Clock by Spaider54")                           #set the title of appe
windowWidth = root.winfo_reqwidth()                        #with of window
windowHeight = root.winfo_reqheight()                      #Height of window
positionRight = int(root.winfo_screenwidth() / 2 -windowWidth )
positionDown = int(root.winfo_screenheight() / 2 -windowHeight )
root.geometry(f"400x200+{positionRight}+{positionDown}")   #set the size of window and 
root.attributes("-fullscreen", False)               
root.configure(background="black")                         #set the background of window black
root.bind("x", quit)                                       #set a button of quit in the top of window[Min,Max]
root.after(1000, clock_time)

fnt = font.Font(family='Roboto', size=50, weight='bold')    # define a font
txt = StringVar()                                           #define a string variable for controle
lb1 = Label(root, textvariable=txt, font=fnt, foreground="white", background="black") # Define Label

lb1.place(relx=0.5, rely=0.5, anchor=CENTER)                #place the label in the center of window
root.mainloop()                                             #run
