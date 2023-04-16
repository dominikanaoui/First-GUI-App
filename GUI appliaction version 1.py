#added checkbox to menu -> file -> program
#added separators

#we import all what is in library tkinter
from tkinter import *
#we import library required to create a message box
import tkinter.messagebox

#we import first library called Tk, we create a window
root = Tk()
#we create another window
#mywindow = Tk()

#we create function for buttons
def button1function():
    #when we type text into text box and click submit it will display this text
    txt1 = txt.get()
    Label(text= txt1, fg='black', bg='grey', font=12).pack()
def button2function():
    Label(text='Opened!', fg='black', bg='grey', font=12).pack()
#we create a function for a "New Project" item in the menu
def gui():
    gu = Tk()
    gu.title("New Project")
    gu.mainloop()
#we create a function for a save item in the menu
def save():
    Label(text='Project saved!', fg='green', bg='white', font=12).pack()
#we create a functions for a message box
def savemessagebox():
    tkinter.messagebox.showinfo('Open', 'File will be open now.')
def close():
    cl = tkinter.messagebox.askquestion('Close','Do you want to close this file?')
    if cl == 'yes':
        root.destroy()

#we create variable txt
txt = StringVar()

#we add a title to out 2nd window
#mywindow.title('Second GUI')
#we add title to our window
root.title('First GUI app in Python')

#we set up size of the window and position of the windows on the screen
root.geometry('500x500+100+200')
#we set up size of the 2nd window and position of the windows on the screen
#mywindow.geometry('500x500+650+200')

#we create class Label
#we call pack; pack is a method, texts Label at the center of the window, on the top
#fg is a colour of the text, bg is a colour of the background
#place method positiones label in x, y position
#grid method positions label in row, column position
#sticky alligns text to W west, E east, N north, S south
mylabel0 = Label(text='First text',fg='white', bg='blue', font=12).pack()
mylabel1 = Label(text='Second text',fg='white', bg='green', font=12).pack()
#mylabel1 = Label(mywindow,text='Second text',fg='white', bg='green', font=12).pack()
#mylabel1 = Label(text='First Text',fg='white', bg='green').place(x=100, y=100)
#mylabel1 = Label(text='First Text',fg='white', bg='green').grid(row=0, column=0, sticky="E")
#mylabel2 = Label(text='Second Text',fg='black', bg='red').grid(row=1, column=0)

#we create a text box
mytext = Entry(textvariable = txt).pack()

#we create button we can click on
Button1 = Button(text= 'Submit', fg='black', bg='white', command = button1function, font=12).pack()
Button2 = Button(text= 'Open', fg='black', bg='white', command= button2function, font=12).pack()

#Button1 = Button(mywindow,text= 'Submit', fg='black', bg='white', command = button1function, font=12).pack()
#Button2 = Button(mywindow,text= 'Open', fg='black', bg='white', command= button2function, font=12).pack()

#we create Menu bar
Chooser = Menu()

#we create menu items
itemone = Menu()
itemone.add_command(label='New Project', command = gui)
itemone.add_command(label='Save', command = save)
itemone.add_command(label='Open', command = savemessagebox)
itemone.add_checkbutton(label='Program')
itemone.add_separator()
itemone.add_radiobutton(label='Dominika')
itemone.add_separator()
itemone.add_command(label='Close', command = close)

itemtwo = Menu()
itemtwo.add_command(label='Copy')
itemtwo.add_command(label='Cut')
itemtwo.add_command(label='Paste')
itemtwo.add_command(label='Delete')

#we create menu bar with names and with menu items
root.config(menu=Chooser)
Chooser.add_cascade(label='File', menu=itemone)
Chooser.add_cascade(label='Edit', menu=itemtwo)
Chooser.add_cascade(label='View')
Chooser.add_cascade(label='Navigate')
Chooser.add_cascade(label='Code')
Chooser.add_cascade(label='Run')
Chooser.add_cascade(label='Tools')
Chooser.add_cascade(label='Help')

#it makes window visible
root.mainloop()
#mywindow.mainloop()
