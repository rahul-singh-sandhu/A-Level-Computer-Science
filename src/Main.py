import ftplib
from ftplib import FTP

connectionChoice = input("Would you like to use a hostname or an IP address? \n")
if connectionChoice == "hostname":
    hostname = input("Please enter an hostname: \n")
    user = input("Please enter a username: \n")
    passwd = input("Please enter a password: \n")
    ftp = FTP(hostname)
    ftp.login(user=user, passwd=passwd)
    print("File List: ")
    files = ftp.dir()
    print(files)
elif connectionChoice == "IP":
    ip = input("Please enter an IP address: \n")
    user = input("Please enter a username: \n")
    passwd = input("Please enter a password: \n")
    ftp = FTP(ip)
    ftp.login(user=user, passwd=passwd)
    print("File List: ")
    files = ftp.dir()
    print(files)