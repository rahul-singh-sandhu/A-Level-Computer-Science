from tkinter import *
from tkinter import ttk
window = Tk()
window.wm_title("Networking Client")
window.resizable(True,True)


def storeIP():
    iphost = ip_hostname.get()
    Label(window, text=f'{iphost}, Registered!', pady=20, bg='#ffbf00').pack()

ip_hostname = Entry(window)
ip_hostname.pack(pady=30)

Button(
    window,
    text="Submit",
    padx=10,
    pady=5,
    command=storeIP
    ).pack

window.mainloop()