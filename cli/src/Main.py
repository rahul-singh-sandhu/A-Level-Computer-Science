import ftplib
from ftplib import FTP

while True:
    hostname = input("Please enter an hostname: \n")
    user = input("Please enter a username: \n")
    passwd = input("Please enter a password: \n")
    try:
        ftp = FTP(hostname)
        ftp.login(user=user, passwd=passwd)
        print("File List: ")
        files = ftp.dir()
        print(files)
    except:
        print("The ftp server could not be reached. Please check your server name, username and password.")
        check = input("Would you like to try again?")
    print(check)
    