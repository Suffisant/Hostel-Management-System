from  tkinter import *
from PIL import ImageTk
import tkinter as tk
from tkinter import ttk

#Function to access new page
def login_page():
    signup_window.destroy()
    import Login

#To get the email given by the user
def email_entry(event):
    if emailEntry.get() == 'Email':
        emailEntry.delete(0, END)

#To get the email given by the user
def username_entry(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)
#to get the password given by the user
def password_entry(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

#To get the confirm password given by the user
def confirmpass_entry(event):
    if confirmpassEntry.get() == 'Confirm Password':
        confirmpassEntry.delete(0, END)

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

#To hide password and change eye icon
def confirm_hide():
    confirm_openeye.config(file = 'closeye.png')
    confirmpassEntry.config(show = '*')
    confirm_eyeButton.config(command = confirm_show)

#To show password and change eye icon
def confirm_show():
    confirm_openeye.config(file = 'openeye.png')
    confirmpassEntry.config(show = '')
    confirm_eyeButton.config(command = confirm_hide)

#GUI part
signup_window = Tk()
signup_window.geometry('985x660+50+50')
signup_window.resizable(False, False)
signup_window.title('Login Page')
bgImage = ImageTk.PhotoImage(file = 'bg1.jpg')
bgLabel = Label(signup_window, image = bgImage)
bgLabel.place(x = 0, y = 0)
#Create account
heading = Label(signup_window, text = 'Create an Account', font = ('times new roman', 20, 'bold', 'italic'), bg = 'white', fg = 'firebrick1')
heading.place(x = 605, y = 116)
#Email
emailEntry = Entry (signup_window, width = 18, font = ('times new roman', 18), bd = 0, fg = 'firebrick1')
emailEntry.place(x = 580, y = 165)
#Email click to remove
emailEntry.insert(0, 'Email')
emailEntry.bind('<FocusIn>', email_entry)
#Email underlineing
Frame(signup_window, width = 250, bg = 'firebrick1').place(x = 580, y = 195)
#Username
usernameEntry = Entry(signup_window , width = 18, font = ('times new roman', 18), bd = 0, fg = 'firebrick1')
usernameEntry.place(x = 580, y = 210)
#username click to remove
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', username_entry)
#Username underlineing
Frame(signup_window, width = 250, bg = 'firebrick1').place(x = 580, y = 240)
#Password
passwordEntry = Entry(signup_window, width = 18, font = ('times new roman', 18), bd = 0, fg = 'firebrick1')
passwordEntry.place(x = 580, y = 255)
#Password click to remove
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_entry)
#To add image at the button
openeye = PhotoImage(file = 'openeye.png')
eyeButton = Button(signup_window, image = openeye, bd = 0, bg = 'white', activebackground = 'white', cursor = 'hand2', command = hide)
eyeButton.place (x = 800,  y = 255)
#Password underlineing
Frame(signup_window, width = 250, bg = 'firebrick1').place(x= 580, y = 285)
#Confirm Password
confirmpassEntry = Entry(signup_window, width = 18, font = ('times new roman', 18), bd = 0, fg = 'firebrick1')
confirmpassEntry.place(x = 580, y = 300)
#Confirm password click to remove
confirmpassEntry.insert(0, 'Confirm Password')
confirmpassEntry.bind('<FocusIn>', confirmpass_entry)
#To add image at the button
confirm_openeye = PhotoImage(file = 'openeye.png')
confirm_eyeButton = Button(signup_window, image = confirm_openeye, bd = 0, bg = 'white', activebackground = 'white', cursor = 'hand2', command = confirm_hide)
confirm_eyeButton.place (x = 800,  y = 300)
#Confirm password underlineing
Frame(signup_window, width = 250, bg = 'firebrick1').place(x = 580, y = 330)
#Drop box option for the user
options = ['Warden', 'Staff', 'Student']
selected_option = tk.StringVar()
selected_option.set('Select the option')
combobox = ttk.Combobox(signup_window, values = options, textvariable = selected_option)
combobox.config(width = 20, font = ('times new roman', 18), foreground = 'firebrick1')
combobox.place(x = 580, y = 345)
#Check button
termsandconditions = Checkbutton(signup_window, text = 'I agree to the Terms and Conditions', font = ('times new roman', 13), bd = 0, bg = 'white', fg = 'firebrick1', activebackground = 'white', activeforeground = 'firebrick1', cursor = 'hand2')
termsandconditions.place(x = 580, y = 390)
#Signup button
signupButton = Button(signup_window, text = 'Signup', font = ('times new roman', 16), bd = 0, bg = 'firebrick1', fg = 'white', activebackground = 'firebrick1', activeforeground = 'white', cursor = 'hand2', width = 17)
signupButton.place(x = 600, y = 425)
#Already account labe 
alreadyaccountLabel = Label(signup_window, text = 'Dont have an account?', font = ('times new roman', 16), bg = 'white', fg = 'firebrick1') 
alreadyaccountLabel.place(x = 580, y = 475)
#Login button
loginButton = Button(signup_window, text ='Login', font = ('times new roman', 16), bg = 'white', fg = 'blue', bd =0, cursor = 'hand2', activebackground = 'white', activeforeground = 'blue', command = login_page)
loginButton.place(x = 780, y = 472)

signup_window.mainloop()