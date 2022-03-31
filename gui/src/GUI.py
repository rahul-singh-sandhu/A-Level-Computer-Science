#importing the libraries
from tkinter import *
from ftplib import *
from tkinter import filedialog
import tkinter as tk
import ftputil
from tkinter import BOTH, END, LEFT
import tkinter
#Test
window = Tk()
window.wm_title("Networking Client")
window.resizable(True,True)
window.configure(bg='white')
window.geometry("1200x800")
window.iconbitmap('src/logo.ico')
text_servermsg = tkinter.Text(window)
text_servermsg.place(x=300,y=150)
#This function is the function that retrives the hostname, username and password that the user enters, and then returns the list of files on the ftp server.
def storeIP():
    #The following variables contain the hostname, username and password.
    ip_host = ip_hostname.get()
    user_login = user.get()
    passwd_login = passwd.get()
    #This function loads the FTP server.
    files = []
    directories = []
    with ftputil.FTPHost(ip_host, user_login, passwd_login) as ftp_host:
        list = ftp_host.listdir(ftp_host.curdir)
        for fname in list:
            if ftp_host.path.isdir(fname):
                directories.append(fname)
                text_servermsg.insert(END, fname + " is a directory")
                text_servermsg.insert(END, "\n")
            else:
                files.append(fname)
                text_servermsg.insert(END, fname + " is not a directory")
                text_servermsg.insert(END, "\n")
    print(*files)
    print(*directories)

def upload():
    pass
def download():
    pass
          
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename)
#This code displays the form
ip_hostname = Entry(window)
ip_hostname.pack(anchor='w',padx=10,pady=30)
ip_hostname.insert(END, 'IP Address')
user = Entry(window)
user.pack(anchor='w',padx=10,pady=30)
user.insert(END, 'Username')
passwd = Entry(window)
passwd.pack(anchor='w',padx=10,pady=30)
passwd.insert(END, 'Password')
passwd.config(show="*")
data = Entry(window)
data.pack(anchor='w', padx=10, pady=30)
data.insert(END, 'File Names')
directory = Entry(window)
directory.pack(anchor='w',padx=10,pady=30)
directory.insert(END, 'Directory')
label_file_explorer = Label(window,
                            text="File Explorer using Tkinter",
                            width=100, height=4,
                            fg="blue")

Button(
    window,
    text="Browse",
    padx=10,
    pady=5,
    width=10,
    command=browseFiles
    ).pack(anchor='w', padx=10)
#This code is for the submit button. It utilises the storeIP() function
Button(
    window,
    text="Submit",
    padx=10,
    pady=5,
    width=10,
    command=storeIP
    ).pack(anchor='w', padx=10)
Button(
    window,
    text="Upload",
    padx=10,
    pady=5,
    width=10,
    command=upload
    ).pack(anchor='w', padx=10)
Button(
    window,
    text="Download",
    padx=10,
    pady=5,
    width=10,
    command=download
    ).pack(anchor='w', padx=10)

window.mainloop()


#Good to see the comments in place :)
