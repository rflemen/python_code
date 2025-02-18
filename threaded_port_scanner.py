# Multithreaded Port Scanner
from queue import Queue
import socket
import threading
import argparse
import pyfiglet
import time
import re


banner = pyfiglet.figlet_format("Port Scanner")
print("\nThreaded...")
print(banner)
print("\t\t\t\t\t\t by Rob Flemen\n")


queue = Queue()
open_ports = []
closed_ports = []


parser = argparse.ArgumentParser()
parser.add_argument("ip_address", help="the ip address to be scanned")
parser.add_argument("-m", "--mode", help="1=Ports 1-1024; 2=Most common ports; 3=All ports", type=int)
args = parser.parse_args()
print(f"The IP to be scanned is: {args.ip_address}")
if args.mode == 1:
    print(f"The mode to be used is: Well known ports (1-1024)\n")
elif args.mode == 2:
    print(f"The mode to be used is: Most common ports\n")
elif args.mode == 3:
    print(f"The mode to be used is: All ports\n")



def validate_ip(ip):
    # Determine if IP addresses is valid IP address. REGEX pattern taken from: 
    # "https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch07s16.html 
    # I did have to add an escape character "\" before the "\." for it to work completely correctly
    pattern = re.compile('''(^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$)''')
    test = pattern.search(ip) 
    if test: # valid IP address
        return True
    else: # invalid IP address
        print("\nInvalid IP address entered. Exiting program.\n")
        exit()


validate_ip(args.ip_address)
target = args.ip_address
scan_mode = args.mode


def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((target, port))
        s.shutdown(2)
        return True
    except:
        return False
    

def get_ports(mode):
    if mode == 1:
        for port in range(1, 1025):
            queue.put(port)
    elif mode == 2:
        ports = [20, 21, 22, 23, 25, 53, 69, 80, 88, 102, 110, 111, 135, 137, 139, 143, 381, 383, 443,
                 445, 464, 465, 587, 593, 636, 691, 902, 989, 990, 993, 1025, 1194, 1337, 1589, 1725, 2082, 
                 3074, 3306, 3389, 3585, 3586, 3724, 4444, 5432, 5900, 6665, 6666, 6667, 6668, 6669, 6881,
                 6970, 6999, 8086, 8087, 8222, 9100, 10000, 12345, 12345, 27374, 31337]
        for port in ports:
            queue.put(port)
    elif mode == 3:
        for port in range(1, 65536):
            queue.put(port) 


def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("[\N{CHECK MARK}]\tPort {} is open!".format(port))
            open_ports.append(port)
        else:
            closed_ports.append(port)


def run_scanner(threads, mode):
    get_ports(mode)
    start = time.time()
    thread_list = []
    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    end = time.time()
    duration = end - start
    print(f"\nStats for {target}:")
    print("--------------------------")
    print(f"[\N{CHECK MARK}]\t{len(open_ports)} ports are open:", open_ports)
    print(f"[!]\t{len(closed_ports)} ports are closed.")
    print(f"[?]\t{len(closed_ports) + len(open_ports)} port scanned in {duration:.2f} seconds.")
    print(f"[?]\tScanned {int(((len(closed_ports) + len(open_ports))/duration))} ports per second.\n")


run_scanner(1800, scan_mode)