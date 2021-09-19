from tkinter import *
from tkinter import ttk
import ftplib
from ftplib import FTP
window = Tk()
window.wm_title("Networking Client")
window.resizable(True,True)


def storeIP():
    ip_host = ip_hostname.get()
    user_login = user.get()
    passwd_login = passwd.get()
    Label(window, text=f'{ip_host}, submitted!', pady=20, bg='#ffbf00').pack()
    ftp = FTP(ip_host)
    ftp.login(user=user_login, passwd=passwd_login)
    print("File List: ")
    files = ftp.dir()
    print(files)

ip_hostname = Entry(window)
ip_hostname.pack(pady=30)
user = Entry(window)
user.pack(pady=30)
passwd = Entry(window)
passwd.pack(pady=30)


Button(
    window,
    text="Submit",
    padx=10,
    pady=5,
    command=storeIP
    ).pack()
window.mainloop()
