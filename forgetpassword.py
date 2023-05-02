from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import pymysql

def change_password():
    if user_entry.get() == '' or newpass_entry.get() == '' or confirmpass_entry.get() == '':
        messagebox.showerror('Error','All fields are required', parent = window)
    elif newpass_entry.get() != confirmpass_entry.get():
        messagebox.showerror('Error','New Password and Confirm Password does not match', parent = window)
    else:
        con = pymysql.connect(host = 'localhost', username = 'root', password = 'P@ssw0rd')
        mycursor = con.cursor()
        query = 'select * from data where username = %s'
        mycursor.execute(query, (user_entry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Incorrect Username', parent = window)
        else:
            query = 'update data set password = %s where username =%s'
            mycursor.execute(query, (newpass_entry.get(), user_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('seccuess', 'Password is reset, Please login with new password', parent = window)
            window.destroy()

#To get the username given by the user
def user_enter(event):
    if user_entry.get() == 'Username':
        user_entry.delete(0, END)

#To get the password given by the user
def password_enter(event):
    if newpass_entry.get() == 'Password':
        newpass_entry.delete(0, END)

#To get the confirm password given by the user
def confirmpassword_enter(event):
    if confirmpass_entry.get() == 'Confirm Password':
        confirmpass_entry.delete(0, END)

#To hide password and change eye icon
def confirm_hide():
    confirm_openeye1.config(file = 'closeeye1.png')
    confirmpass_entry.config(show = '*')
    confirm_eyeButton.config(command = confirm_show)

#To show password and change eye icon
def confirm_show():
    confirm_openeye1.config(file = 'openeye1.png')
    confirmpass_entry.config(show = '')
    confirm_eyeButton.config(command = confirm_hide)

#To hide password and change eye icon
def hide():
    openeye1.config(file = 'closeeye1.png')
    newpass_entry.config(show = '*')
    eyeButton.config(command = show)

#To show password and change eye icon
def show():
    openeye1.config(file = 'openeye1.png')
    newpass_entry.config(show = '')
    eyeButton.config(command = hide)

#GUI Part
window = Toplevel()
window.title("Change Password")
window.resizable(False,False)
#Background image
bgPic = ImageTk.PhotoImage(file = 'background.jpg')
bgLabel = Label(window, image = bgPic)
bgLabel.grid()
#Heading for Forget Password
heading_label = Label(window, text = 'Reset Password', font = ('times new roman', 20, 'bold', 'italic'), bg = 'white', fg = 'magenta2')
heading_label.place(x = 480, y = 60)
#Username of forget password label, underlineline and entry
user_entry = Entry(window, width = 20, fg = 'magenta2', font = ('times new roman', 18), bd =0)
user_entry.place(x = 470, y = 120)
Frame(window, width = 250, height = 2, bg = 'orchid1').place(x = 470, y = 145)
#user login click to remove
user_entry.insert(0, 'Username')
user_entry.bind('<FocusIn>', user_enter)
#Password of forget password label, underlineline and entry
newpass_entry = Entry(window, width = 20, fg = 'magenta2', font = ('times new roman', 18), bd = 0)
newpass_entry.place(x = 470, y = 170)
Frame(window, width = 250, height = 2, bg = 'orchid1').place(x = 470, y = 195)
#Password click to remove
newpass_entry.insert(0, 'Password')
newpass_entry.bind('<FocusIn>', password_enter)
#To add image at the button
openeye1 = PhotoImage(file = 'openeye1.png')
eyeButton = Button(window, image = openeye1, bd = 0, bg = 'white', activebackground = 'white', cursor = 'hand2', command = hide)
eyeButton.place (x = 695,  y = 165)
#Confirm password of forget password label, underlineline and entry
confirmpass_entry = Entry(window, width = 20, fg = 'magenta2', font = ('times new roman', 18), bd = 0)
confirmpass_entry.place(x = 470, y = 220)
Frame(window, width = 250, height = 2, bg = 'orchid1').place(x = 470, y = 245)
#Confirm Password click to remove
confirmpass_entry.insert(0, 'Confirm Password')
confirmpass_entry.bind('<FocusIn>', confirmpassword_enter)
#To add image at the button
confirm_openeye1 = PhotoImage(file = 'openeye1.png')
confirm_eyeButton = Button(window, image = confirm_openeye1, bd = 0, bg = 'white', activebackground = 'white', cursor = 'hand2', command = confirm_hide)
confirm_eyeButton.place (x = 695,  y = 218)
#Drop box option for the user
options = ['Warden', 'Staff', 'Student']
selected_option = tk.StringVar()
selected_option.set('Select the option')
combobox = ttk.Combobox(window, values = options, textvariable = selected_option)
combobox.config(width = 20, font = ('times new roman', 16), foreground = 'orchid1')
combobox.place(x = 470, y = 285)
#Submit Button
submitButton = Button(window, text = 'Submit', bd =0, bg = 'magenta2', fg = 'white', font = ('times new roman', 20), width = 17, cursor = 'hand2', activebackground = 'magenta2', activeforeground = 'white', command = change_password)
submitButton.place(x = 470, y = 390)

window.mainloop()