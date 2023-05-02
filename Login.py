from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import pymysql

#Function and window for Forget password
def forget_pass():
    import forgetpassword

#Function login button
def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() =='':   #Checking if the user entered both password and username or not
        messagebox.showerror('Error', 'All fields are required')
    else:
        try:
            con = pymysql.connect(host = 'localhost', user = 'root', password = 'P@ssw0rd')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established try again')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username = %s and password = %s'
        mycursor.execute(query,(usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Sucess', 'Login is sucessful')

#Function to access new page
def signup_page():
    login_window.destroy()
    import signup

#To hide password and change eye icon
def hide():
    openeye.config(file = 'closeye.png')
    passwordEntry.config(show = '*')
    eyeButton.config(command = show)

#To show password and change eye icon
def show():
    openeye.config(file = 'openeye.png')
    passwordEntry.config(show = '')
    eyeButton.config(command = hide)

#To get the username given by the user
def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

#To get the password given by the user
def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

#GUI Part
login_window = Tk()
login_window.geometry('985x660+50+50')
login_window.resizable(False, False)
login_window.title('Login Page')
bgImage = ImageTk.PhotoImage(file = 'bg1.jpg')
bgLabel = Label(login_window, image = bgImage)
bgLabel.place(x = 0, y = 0)
#Heading
heading = Label(login_window, text = 'User Login', font = ('times new roman', 30, 'bold', 'italic'), bg = 'white', fg = 'firebrick1')
heading.place(x = 605, y = 130)
#Username
usernameEntry = Entry(login_window, width = 20, font = ('times new roman', 18), bd = 0, fg = 'firebrick1')
usernameEntry.place(x= 580, y= 205)
#user login click to remove
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)
#User login underlineing
frame1 = Frame(login_window, width = 250, bg = 'firebrick1')
frame1.place(x = 580, y = 230)
#Password 
passwordEntry = Entry(login_window, width = 20, font = ('times new roman', 18), bd = 0, fg = 'firebrick1')
passwordEntry.place(x= 580, y= 253)
#Password click to remove
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)
#Underlineing under the password
frame2 = Frame(login_window, width = 250, bg = 'firebrick1')
frame2.place(x = 580, y = 280)
#To add image at the button
openeye = PhotoImage(file = 'openeye.png')
eyeButton = Button(login_window, image = openeye, bd = 0, bg = 'white', activebackground = 'white', cursor = 'hand2', command = hide)
eyeButton.place (x = 800,  y = 253)
#Drop box option for the user
options = ['Warden', 'Staff', 'Student']
selected_option = tk.StringVar()
selected_option.set('Select option')
combobox = ttk.Combobox(login_window, values = options, textvariable = selected_option)
combobox.config(width = 20, font = ('times new roman', 18), foreground = 'firebrick1')
combobox.place(x = 580, y = 300)
#Forgot password button
forgetButton = Button(login_window, text = 'Forget Passsword?', bd = 0, bg = 'white', fg = 'firebrick1', activebackground = 'white', font = ('times new roman', 16), activeforeground = 'firebrick1', cursor = 'hand2', command = forget_pass)
forgetButton.place(x = 680, y = 383)
#Login button
loginButton = Button (login_window, text = ' Login', font = ('times new roman', 18), fg = 'white', activebackground = 'firebrick1', activeforeground = 'white', cursor = 'hand2', width = 19, bd =0, bg = 'firebrick1', command = login_user)
loginButton.place(x = 578, y = 425)
#New account button
newaccountButton = Button (login_window, text = 'Create one',  font = ('times new roman', 14), fg = 'blue', activebackground = 'white', activeforeground = 'blue', bg = 'white', cursor = 'hand2', width = 11, bd =0, command = signup_page)
newaccountButton.place(x = 730, y = 491)
#SignupLabel
signupLabel = Label(login_window, text = 'Dont have an account?', font = ('times new roman', 14), fg = 'firebrick1', bg = 'white')
signupLabel.place(x = 565, y = 495)

login_window.mainloop()