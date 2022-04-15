#!/usr/bin/python3
#import the libraries
import os
from requests import get
import time
from requests import exceptions
import sys
import phonenumbers
from phonenumbers import carrier

#checks if you have defined a wordlist for the scan
def checkargv():
    if len(sys.argv) != 2:
        sys.exit("\33[91m[*] You haven't defined a wordlist!!\33[0m")
    else:
        print("\33[92m[*] Wordlist detected!!\33[0m")

#checks if internet connection is available
def internetConnection():
    try:
        get("http://google.com", timeout = 3)
        print("\33[92m[*] Internet is Connected!!\33[0m")
    except exceptions.ConnectionError:
            print("\33[31m[*] Internet Not Connected")

#checks if you are root(it's not necessary, just a little adition)
def checkroot():
    if not os.getuid()==0:
        sys.exit("\33[31m[*] You're NOT root!!\33[0m")
    else:
        print("\33[92m[*] Root access detected!!\33[0m")

#clear all the previous input/output
def clear():
    os.system("clear")
clear()

#start all the above functions
time.sleep(1)
checkargv()
time.sleep(1)
internetConnection()
time.sleep(1)
checkroot()
os.system("clear")


#reads the word list which you defined
def wordlist():
    line = open(sys.argv[1])
    for lines in line:
        lines = lines.strip('\n')
        
#scans the phone number + the carrier       
        phoneNumber = phonenumbers.parse(lines)
        Carrier = carrier.name_for_number(phoneNumber, 'en')
        print("\33[33m[*] Carrier For " + lines + "\33[33m is \33[0m" + Carrier)
wordlist()


