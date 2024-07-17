# Simple Python Port Scanner

## Overview

This is a simple port scanner built using Python. The tool scans specified ports on target machines to check if they are open. It is useful for educational purposes, such as learning about network security, socket programming, and ethical hacking.

## Features

- Scans single or multiple targets.
- Uses Python's socket module for network connections.
- Easy to use and modify.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/port-scanner.git
    cd port-scanner
    ```

2. Install required packages:
    ```bash
    pip install termcolor
    ```

3. Run the script:
    ```bash
    python portScanner.py
    ```

4. Follow the prompts to enter target IP addresses and the number of ports to scan.

## Example

```python
import socket
import termcolor

def scan(target, ports):
    print('\n' + ' Starting Scan For ' + str(target))
    for port in range(1, ports + 1):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port open " + str(port))
        sock.close()
    except:
        pass

targets = input("[*] Enter targets to scan (SPLIT THEM WITH ,): ")
ports = int(input("[*] Enter how many ports you want to scan: "))

if ',' in targets:
    print(termcolor.colored("Scanning multiple targets", 'green'))
    for ipAdd in targets.split(','):
        scan(ipAdd.strip(' '), ports)
else:
    print(termcolor.colored("Scanning single target", 'green'))
    scan(targets, ports)
```

## Disclamer

This tool is intended for educational purposes only. Always ensure you have permission before scanning any network or device. Unauthorized scanning is illegal and unethical.
