import socket
import termcolor

def scan(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports):
		scan_port(target,port)

def scan_port(ipaddress, port):
        try:
                sock = socket.socket()
                sock.connect((ipaddress, port))
                print("[+] Port open " + str(port))
                sock.close()
        except:
                pass


targets = input("[*] Enter targets to scan (SPLIT THEM WITH ,: ")
ports = int(input("[*] Enter how many ports you want to scan (SPLIT THEM WITH ,: "))

if ',' in targets:
        print(termcolor.colored(("Scanning multiple targets"), 'green'))
        for ipAdd in targets.split(','):
         	scan(ipAdd.strip(' '), ports)
else:
        print(targets)
        scan(targets, ports)

