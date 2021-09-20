#importing the libraries
from tkinter import *
from tkinter import ttk
import ftplib
from ftplib import FTP

#This function creates the tkinter windows.
import background
import self as self

window = Tk()
window.wm_title("Networking Client")
window.resizable(True,True)
window.configure(bg='white')
window.geometry("200x300")


#This function is the function that retrives the hostname, username and password that the user enters, and then returns the list of files on the ftp server.
def storeIP():
    #The following variables contain the hostname, username and password.
    ip_host = ip_hostname.get()
    user_login = user.get()
    passwd_login = passwd.get()
    #This prints the submission message.
    Label(window, text=f'{ip_host} submitted!', pady=20, bg='lightgray').pack()
    #This function loads the FTP server.
    ftp = FTP(ip_host)
    ftp.login(user=user_login, passwd=passwd_login)
    #This function prints the directory structure.
    print("File List: ")
    files = ftp.dir()
    print(files)
def upload():
    ip_host = ip_hostname.get()
    user_login = user.get()
    passwd_login = passwd.get()
    ftp = ftplib.FTP(ip_host, user_login, passwd_login)
    file = open('Testdoc.rtf', 'rb')  # file to send
    ftp.storbinary('STOR Testdoc.rtf', file)  # send the file
    print("File List: ")
    files = ftp.dir()
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

#This code is for the submit button. It utilises the storeIP() function
Button(
    window,
    text="Submit",
    padx=10,
    pady=5,
    command=storeIP
    ).pack(anchor='w', padx=10)
Button(
    window,
    text="Upload",
    padx=10,
    pady=5,
    command=upload
    ).pack(anchor='w', padx=10)
window.mainloop()


#Good to see the comments in :)
