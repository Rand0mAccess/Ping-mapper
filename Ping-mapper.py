import termcolor
import re
import os



print("""\
    
    
██████╗ ██╗███╗   ██╗ ██████╗     ███╗   ███╗ █████╗ ██████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██║████╗  ██║██╔════╝     ████╗ ████║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝██║██╔██╗ ██║██║  ███╗    ██╔████╔██║███████║██████╔╝██████╔╝█████╗  ██████╔╝
██╔═══╝ ██║██║╚██╗██║██║   ██║    ██║╚██╔╝██║██╔══██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
██║     ██║██║ ╚████║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║██║     ██║     ███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                       """)
                                                                                       

# Validating IP

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

try:
    while True:
        target = input("[*] Enter Targets IP To Scan : ")
        if (re.search(regex, target)):
            lol = "ping -c1 %s > raw.txt"%(target)
            os.system(lol)
            break
        else:
            print('Please enter the valid ip')
            continue
except:
    print('error')	 




#checking for OS with ttl value

def OS(file):
    f = open(file, 'r')
    for line in f:
        if 'ttl=128' in line:
            print('windows server')
        elif 'ttl=255' in line:
            print('It is a Linux kernel 2.4')
        elif 'ttl=64' in line:
            print('It is a Linux kernel 4.10 ')

OS('raw.txt')

print('Now have some patience while Ping mapper is mapping the IP')
# Doing the nmap scan

def map(file):
    n = open(file, 'r')
    for word in n:
        if 'up' in word:
            nmap = "nmap -sC -sV -p- --script=vuln %s > results.txt"%(target)
            os.system(nmap)
        else:
            pass    

map('raw.txt')
	 
os.system('rm -r raw.txt')		

print('JOB DONE BOSS!!!')


