import ftplib
from ftplib import FTP

connectionChoice = input("Would you like to use a hostname or an IP address?")
if connectionChoice == "hostname":
    ip = input("Please enter an hostname: \n")
elif connectionChoice == "IP":
    ip = int(input("Please enter an IP address: \n"))

ftp = FTP('ftp.dlptest.com')
ftp.login(user='dlpuser', passwd ='rNrKYTX9g7z3RgJRmxWuGHbeu')
print("File List: ")
files = ftp.dir()
print(files)
