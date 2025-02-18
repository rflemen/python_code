# Multithreaded Port Scanner
from queue import Queue
import socket
import threading
import argparse
import pyfiglet
import time


banner = pyfiglet.figlet_format("Port Scanner")
print("\nThreaded...")
print(banner)
print("\t\t\t\t\t\t by Rob Flemen\n")


queue = Queue()
open_ports = []
closed_ports = []


parser = argparse.ArgumentParser()
parser.add_argument("ip_address", help="the ip address to be scanned")
parser.add_argument("-m", "--mode", help="1 = ports 1-1024; 2 = all 65535 ports; 3 = most common ports", type=int)
args = parser.parse_args()
print(f"The IP to be scanned is: {args.ip_address}")
if args.mode == 1:
    print(f"The mode to be used is: Top 1024 ports\n")
elif args.mode == 2:
    print(f"The mode to be used is: All 65535 ports\n")
elif args.mode == 3:
    print(f"The mode to be used is: Most common ports\n")


target = args.ip_address
scanMode = args.mode


def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        for port in range(1, 65536):
            queue.put(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 111, 139, 443, 445, 3306, 3389]
        for port in ports:
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

run_scanner(1800, scanMode)