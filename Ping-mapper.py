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


try:
    while True:
        target = input(termcolor.colored("[*] Enter Targets To Scan (split them by ,): ", 'red'))
        octet_ip = target.split(".")
        int_octet_ip = [int(i) for i in octet_ip]
        if len(int_octet_ip) == 4:
            print('ok')
            break
        else:
            print('Please enter the valid ip')
            continue
except:
    print('error')
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in target:
    print('[*] Scanning Multiple Targets')
    for ip_addr in target.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(target, ports)