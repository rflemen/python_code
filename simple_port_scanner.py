# A simple multithreaded port scanner written by Rob Flemen
import pyfiglet
import re
import argparse
 
banner = pyfiglet.figlet_format("Simple Port Scanner")
print(banner)
print("\t\t\t by Rob Flemen\n")


#Take filename as argument
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the file to be read")
parser.add_argument("-p", "--port", help="the port to be scanned", type=int)
parser.add_argument("-n", "--name", help="the name of the person running the program")
args = parser.parse_args()
print("The filename read in is:", args.filename)
print("The port to be scanned is:", args.port)
print("The name of the person running the program is:", args.name)

# Argument (file name) fed to variable
filename = args.filename
username = args.name
port = args.port


# Read from a file (this will be for reading IP addresses to scan)
try:
    with open(filename) as file_object:
        ips = file_object.readlines()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")


# Determion if IP addresses in file are valid IP addresses:
# REGEX pattern taken from "https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch07s16.html 
# I did have to add an escape character "\" before the "\." for it to work completely correctly
pattern = re.compile('''(^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$)''')
valid =[] 
invalid=[] 


for ip in ips: 
    ip = ip.rstrip() 
    result = pattern.search(ip) 
    # valid IP addresses 
    if result: 
      valid.append(ip) 
    # invalid IP addresses   
    else: 
      invalid.append(ip) 
  

# Displaying the IP addresses (just for debugging) 
print("Valid IPs") 
print(valid)

print("Invalid IPs") 
print(invalid) 







