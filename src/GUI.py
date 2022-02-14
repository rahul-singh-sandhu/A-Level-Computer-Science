#importing the libraries
from tkinter import *
from ftplib import *
from tkinter import filedialog

print("Hello this is Rich")

window = Tk()
window.wm_title("Networking Client")
window.resizable(True,True)
window.configure(bg='white')
window.geometry("200x430")

#This function is the function that retrives the hostname, username and password that the user enters, and then returns the list of files on the ftp server.
def storeIP():
    #The following variables contain the hostname, username and password.
    ip_host = ip_hostname.get()
    user_login = user.get()
    passwd_login = passwd.get()
    directory_path = directory.get()
    #This function loads the FTP server.
    ftp = FTP(ip_host)
    ftp.login(user=user_login, passwd=passwd_login)
    #This function prints the directory structure.
    print("File List: ")
    files = ftp.dir()
    print(files)
def upload():
    filename = data.get()
    ip_host = ip_hostname.get()
    user_login = user.get()
    passwd_login = passwd.get()
    ftp = ftplib.FTP(ip_host, user_login, passwd_login)
    with open(filename, "rb") as file:
        ftp.storbinary(f"STOR {filename}", file)
    print("File List: ")
    files = ftp.dir()
    print(files)
def download():
    filename = data.get()
    ip_host = ip_hostname.get()
    user_login = user.get()
    passwd_login = passwd.get()
    ftp = ftplib.FTP(ip_host, user_login, passwd_login)
    with open(filename, "wb") as file:
        ftp.retrbinary(f"RETR {filename}", file.write)
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
