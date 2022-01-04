import socket
import termcolor


def scan(target, ports):
    print('\n' + termcolor.colored((" Starting Scan For"), 'green') + str(target))
    for port in range(1, ports):
        scan_port(target, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        pass


# Python program to validate an Ip address
import re

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def check(Ip):
	if(re.search(regex, Ip)):
		print("Valid Ip address")
	else:
		print("Invalid Ip address")
	
Ip = input("Enter the ip address :")
check(Ip)


ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
'''if ',' in target:
    print('[*] Scanning Multiple Targets')
    for ip_addr in target.split(','):
        scan(ip_addr.strip(' '), ports)'''
else:
    scan(target, ports)
