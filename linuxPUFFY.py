
import json
import getpass
import time
import os
import socket
import sys
import subprocess
import requests
import urllib.request
import threading
from concurrent.futures import ThreadPoolExecutor
import random
import hashlib
import secrets
import platform
import random
import string



#ANSII codes for coloring in the terminal
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
ORANGE = "\033[38;2;255;165;0m"
PURPLE = "\033[35m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"



DATA_FILE = "PUFFYpw.json" 

VENDOR_CACHE = {} # cache to save API calls
api_lock = threading.Lock() # Thread lock to ensure thread-safe API access during multi threaded sweeps


#hash selection for getHash()
HASH_FUNCTIONS = {
    "1": ("SHA-256", hashlib.sha256),
    "2": ("SHA-512", hashlib.sha512),
    "3": ("SHA-1", hashlib.sha1),
    "4": ("MD5", hashlib.md5),
    "5": ("SHA-384", hashlib.sha384),
    "6": ("SHA-224", hashlib.sha224),
    "7": ("SHA3-256", hashlib.sha3_256),
    "8": ("SHA3-512", hashlib.sha3_512),
    "9": ("BLAKE2b", hashlib.blake2b),
}


         

#ports for portSCAN()
ports = {
    21: "FTP - File Transfer Protocol",
    23: "Telnet - Remote Access Encrypted",
    22: "SSH - Secure Shell (Remote Access)",
    25: "SMTP - Simple Mail Transfer Protocol (E-Mail)",
    80: "HTTP - Hyper Text Transfer Protocol (Web)",
    135: "RPC - Remote Procedure Call",
    139: "NetBIOS - Windows Network Sharing",
    443: "HTTPS - HTTP secure (Encrypted Web)",
    445: "SMB - Server Message Block (File Sharing)",
    554: "RTSP - Real Time Streaming Protocol (Camera Stream)",
    3306: "MySQL - Database",
    3389: "RDP - Remote Desktop Protocol",
    8080: "HTTP-Alt - Alternative Web Port"
}






def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def countdown(seconds=5):
    for i in range(seconds, 0, -1):
        print(f"\r[*] Continuing in: {i} ", end="", flush=True)
        time.sleep(1)



def portScanAnim(target):
    for _ in range(3):
        for dots in [".", "..", "..."]:
            sys.stdout.write(f"\r[*] Preparing to scan {target} {dots}        ")
            sys.stdout.flush()
            time.sleep(0.4)
           


def netSweepAnim(network):
    for _ in range(3):
        for dots in [".", "..", "..."]:
            sys.stdout.write(f"\r[*] Preparing to sweep {network} {dots}      ")
            sys.stdout.flush()
            time.sleep(0.4)














def password():
    if os.path.exists(DATA_FILE):
        login()
    else:
            print("[-] Password not found.")
            save_password = input("[?] Create a password: ")
            text_bytes = save_password.encode("utf-8")
            hash_object = hashlib.sha256(text_bytes).hexdigest()


            #calls the save func and saves hash
            save_user_data(save_password, hash_object)

            print("Password saved! Redirecting to Log-in...")
            time.sleep(2)
            clear_screen()
            login()


def save_user_data(password, password_hash):
    try:
        password = "encrypted!"
        data = {"password": password, "hash": password_hash}
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4) #transforms the dictionary 'data' into JSON-text, writes it into the file 'f' and sets the indent to a comfortable reading format
    except Exception as e:
        print(f"Error: {e}")
                    
           

def login():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            stored_data = json.load(file)
            
        while True:
            print(f"{YELLOW}𝖯𝖴𝖥𝖥𝖸 𝖬𝖴𝖫𝖳𝖨𝖳𝖮𝖮𝖫{RESET}")
            print("by puffy\n")
            quest = getpass.getpass("[?] Enter your Password: ", stream=None)
            text_bytes = quest.encode("utf-8")
            input_hash = hashlib.sha256(text_bytes).hexdigest()

            if input_hash != stored_data["hash"]:
                print("[-] Wrong password! Try again.")
                time.sleep(1.1)
                clear_screen()
                continue  
            else:
                print(f"{GREEN}Access Approved...{RESET}")
                time.sleep(1.4)
                clear_screen()
                choice()
                break
    except FileNotFoundError:
        print("[!] No password file found. Please set up a password first.")
        time.sleep(2)
        password()
    

  

      
     


def choice(): #main navigation
    while True:
        print(fr"""{YELLOW}
______ _   _______________   __     ___  ____   _ _    _____ _____ _____ _____  _____ _     
| ___ \ | | |  ___|  ___\ \ / /     |  \/  | | | | |  |_   _|_   _|_   _|  _  ||  _  | |    
| |_/ / | | | |_  | |_   \ V /      | .  . | | | | |    | |   | |   | | | | | || | | | |    
|  __/| | | |  _| |  _|   \ /       | |\/| | | | | |    | |   | |   | | | | | || | | | |    
| |   | |_| | |   | |     | |       | |  | | |_| | |____| |  _| |_  | | \ \_/ /\ \_/ / |____
\_|    \___/\_|   \_|     \_/       \_|  |_/\___/\_____/\_/  \___/  \_/  \___/  \___/\_____/
{RESET}""")
        ch = input(f"\nWhich tool would you like to use?\n\n1: Port Scanner\n2: Network Sweeper\n3: IP Geolocation Tracker\n4: Hash Cracker\n5: Username and Password generator\n\n{YELLOW}------------------{RESET}\n6: Game\n7: Exit the program\n\nYour choice: ")
        if ch == "1":
            clear_screen()
            portSCAN()
        elif ch == "2":
            clear_screen()
            netSWEEP()
        elif ch == "3":
            clear_screen()
            geoTRACK()
        elif ch == "4":
            clear_screen()
            hashCrack()
        elif ch == "5":
            clear_screen()
            pwgen()
        elif ch == "6":
            clear_screen()
            agame()
        elif ch == "7":
            print(f"\n{YELLOW}Goodbye!{RESET}")
            time.sleep(1.4)
            clear_screen()
            sys.exit()
        else:
            print(f"{RED}[-] Your choice was invalid, please try again.{RESET}")
            clear_screen()
            time.sleep(2)
            continue



def getVendor(mac): # fetches hardware vendor for a given mac address via online API
    if mac == "Unknown MAC" or mac == "<incomplete>" or not mac:
        return "[!] Unknown Vendor"
    
    # Load from cache if already resolved
    if mac in VENDOR_CACHE:
        return VENDOR_CACHE[mac]
    with api_lock:
       try:
           time.sleep(1.5)
        
           url = f"https://api.macvendors.com/{mac}"
           # Send User Agent header to prevent anti bot blocking
           req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
           response = urllib.request.urlopen(req, timeout=3)
           vendor_name = response.read().decode().strip()
        
           # Save to cache
           VENDOR_CACHE[mac] = vendor_name
           return vendor_name
       except urllib.error.HTTPError as e:
           if e.code == 429: # Error 429 = Too Many Requests
               return "[!] Unknown Vendor (Rate Limited)"
       except:
           pass
       return "[!] Unknown Vendor"




def getMac(ip): #reads the mac address from the local cache (in here linux ARP cache with 'ip neigh')
    try:
        result = subprocess.check_output("ip neigh", shell=True).decode()
        for line in result.split('\n'):
            if ip in line and "lladdr" in line:
                parts = line.split()
                if "lladdr" in parts:
                    idx = parts.index("lladdr")
                    if len(parts) > idx + 1:
                        return parts[idx + 1] # MAC address follows right after 'lladdr'
    except:
        pass
    return "Unknown MAC"





def banner_grabber(target, port): # connects to an open port and extracts software details known as banners 

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)
        s.connect((target, port))

        # Specialized payload for Web servers (HTTP)
        if port in [80, 8080]:
            s.sendall(b"HEAD / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
            response = s.recv(1024).decode("utf-8", errors="ignore")
            s.close()
            
            for line in response.split("\n"):
                if "Server:" in line:
                    return line.replace("Server:", "").strip()
            return "Webserver"

        else:
            # Capture standard banner response (e.g., SSH/FTP version)
            banner = s.recv(1024).decode("utf-8", errors="ignore").strip()
            s.close()
            if banner:
                return banner
            else:
                return "No Banner response"
    except:
        return "Unknown / Shielded"


def portSCAN(): 
    print(f"{YELLOW}PUFFY PORT SCANNER{RESET}")
    target = input("[?] Enter the target IP or website you would like to port scan: ")
    
    # Port selection phase (single port or default range 1-1023)
    while True:
        user_port = input("[?] Enter a specific port to scan (Press enter to scan all / 1-1023): ")
        if user_port == "":
            port_range = range(1, 1024)
            break
        try:
            single_port = int(user_port)
            port_range = [single_port]
            break
        except ValueError:
            print(f"{RED}[-] Please enter a valid number or press enter!{RESET}")

    
    # Resolve domain names example google.com to an IPv4 address
    try:
        target = socket.gethostbyname(target)
        print(f"\nTarget IP: {target}")
    except socket.gaierror:
        print(f"{RED}[!] Invalid IP or hostname. Exiting the tool ...{RESET}")
        return

    portScanAnim(target)
    if user_port == "":
        print("\n[*] Starting the scan!")
    
    else:
        print(f"\n[*] Starting the scan for Port {RED}{user_port}{RESET} only!")
        

    scan_results = []
    for port in port_range:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        # connect_ex returns 0 if the port is OPEN
        result = s.connect_ex((target, port))
        if result == 0:
            service = ports.get(port, "Unknown Port")
            s.close()

            banner = banner_grabber(target, port)
            output_line = f"Port {port} is open! | {service} | Software: {banner}"
            print(output_line)
            scan_results.append(output_line)
        else:
            s.close()
    
    print(f"{GREEN}[+] Scan finished!{RESET}")
    save_results(scan_results, f"Port Scan for {target}")







def fast_sweep(ip): #pings an ip, if active resolves hostname, mac and vendor metadata
    response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1") # '> /dev/null 2>&1' silences console output from the ping command
    if response == 0:
        mac = getMac(ip)
        vendor = getVendor(mac)
        
        try:
            hostname = socket.gethostbyaddr(ip)
            return f"[+] Device found: {ip} | {hostname[0]} | MAC: {mac} | Vendor: {vendor}"
        except:
            return f"[+] Device found: {ip} | Unknown Hostname | MAC: {mac} | Vendor: {vendor}"
    return None


def netSWEEP(): # sweeps an entire subnet from 1-254 for active hosts using multithreading
    print(f"\n{YELLOW}PUFFY NETWORK SWEEPER{RESET}")
    network = input("[?] Enter the network IP (MUST END WITH A DOT): ")

    netSweepAnim(network)
    print("\rStarting the sweep!             ")

    ip_list = [network + str(i) for i in range(1, 255)]
    sweep_results = []

    # Spawns 30 concurrent threads for fast ping scanning
    with ThreadPoolExecutor(max_workers=30) as executor:
        results = executor.map(fast_sweep, ip_list)

        for result in results:
            if result:
                print(result)
                sweep_results.append(result)

    print(f"{GREEN}[+] Sweep finished!{RESET}")
    save_results(sweep_results, f"Network Sweep for {network}x")








def geoTRACK(): # gets geolocation and isp data for a public ip address
    print(f"\n{YELLOW}PUFFY IP GEOLOCATION TRACKER{RESET}")
    tip = input("[?] Enter the public IP address to track: ")

    url = f"http://ip-api.com/json/{tip}"
    track_results = []
    clear_screen()
    try: 
        response = requests.get(url, timeout=5)
        data = response.json()


        if data.get("status") == "success":
            results_to_save = [
                f"Country: {data.get('country')}",
                f"Region: {data.get('region')} | {data.get('regionName')}",
                f"City: {data.get('city')}",
                f"Timezone: {data.get('timezone')}",
                f"ISP: {data.get('isp')}",
                "----------------------------------------------------------",
                f"Mobile? {data.get('mobile')}",
                f"Proxy? {data.get('proxy')}",
                f"Hosting? {data.get('hosting')}"
            ]
            
            print("\n")
            for line in results_to_save:
                print(line)
                
            track_results.extend(results_to_save)

        else:
            print(f"{RED}[!] IP address could not be located.{RESET}")
    except Exception as e:
                print(f"{RED}[!] Connection error: {e}{RESET}")
    print(f"\n[+] Geolocation track for: {tip} finished.")
    save_results(track_results, f"Geomap results for: {tip}")






def hashCrack():
    print(f"\n{YELLOW}PUFFY HASH CRACKER{RESET}")

    print("\n=== AVAILABLE HASH TYPES ===\n")
    for key, (name, _) in HASH_FUNCTIONS.items():
        print(f"  {key}. {name}")

    while True:
        hashChoice = input("\n[?] Select hash type (1-9): ").strip().lower()
        if hashChoice in HASH_FUNCTIONS:
            hash_name, hash_func = HASH_FUNCTIONS[hashChoice]
            print(f"\n[*] Selected: {hash_name}")
            break
        else:
            print("[-] Invalid choice, please try again!")
            time.sleep(1.4)
            clear_screen()
            continue
    
    target_hash = input(f"\n[?] Enter the {hash_name} target hash: ").strip()
    if not target_hash:
        print("[-] No hash entered. Exiting.")
        sys.exit(1)
    
    wordlist_path = input("[?] Enter path to wordlist: ").strip()
    if not wordlist_path:
        print("[-] No wordlist path entered. Exiting.")
        sys.exit(1)

    print(f"\n[*] Attempting to crack {hash_name} hash: {target_hash}")
    print(f"[*] Using wordlist: {wordlist_path}\n")

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line_number, word in enumerate(file, 1):
                password = word.strip()
            
            
            word_bytes = password.encode('utf-8')
            candidate_hash = hash_func(word_bytes).hexdigest()


            if candidate_hash == target_hash:
                print(f"[+] MATCH FOUND (Line {line_number})!")
                print(f"[+] Target Hash : {target_hash}")
                print(f"[+] Password    : {password}")
                return

            
            #Show progress every 10000 lines
            if line_number % 10000 == 0:
                print(f"[*] Progress: {line_number} lines checked...", end ="\r")

        print("\n[-] Finished: Password not found in wordlist.")
        return None     

    except FileNotFoundError:
        print(f"\n[!] Error: File '{wordlist_path}' was not found!")
        print("[!] Make sure the file exists and the path is correct.")
        
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] An unexpected error occurred: {e}")
          
            



def pwgen():
    print(f"\n{YELLOW}PUFFY GENERATOR{RESET}")

  # Define characters allowed for usernames (lowercase letters + numbers)
    chars_user = string.ascii_lowercase + string.digits 

  # Define characters allowed for passwords (all letters + numbers + special symbols)
    chars_pass = string.ascii_letters + string.digits + string.punctuation

    while True:
        ch = input("Choose what you would like to generate? (1: Username , 2: Password): ")

        length = None
        char_set = "" # Initialize 'char_set' to empty string to track which characters to use


        if ch == "1":
            try:
                length = int(input("Enter how long your username should be: "))
                char_set = chars_user
            except ValueError:
                print("Please enter a valid number!")
                continue

        elif ch == "2":
            try:
                length = int(input("Enter how long your Password should be: "))
                char_set = chars_pass
            except ValueError:
                print("Please enter a valid Number!")
                continue
        
        else:
            print("Invalid choice! Please try again.")
            continue

        if length is None or length <= 0:
            print("Please enter a positive number!")
            continue

        if ch == "2":
                    result = "".join(secrets.choice(chars_pass) for _ in range(length))
        if ch == "1":
                    result = "".join(random.choice(chars_user) for _ in range(length))

        print(f"Generated: {result}")
        
        again = input("\nGenerate again? (Y/n): ")
        if again.lower() != 'y':
            break
        print("-" * 30)








def agame():
    print(f"\n{GREEN}Arrow Prediction game{RESET}, {RED}where will the arrow go?{RESET}\n♯type 3 anytime to exit♯\n")
    directions = ["r", "l", "f"]
    arrow_symbols = {
        "r": "→ Right",
        "l": "← Left",
        "f": "↑ Forward"
    }

    while True:
        randomi = random.randint(0, 2)
        rdirection = directions[randomi]
    
        choice = input(f"{CYAN}===>{RESET}\n r = right| l = left| f = forward : ").strip().lower()

        if choice == "3":
            print("\nok bye ")
            time.sleep(1.6)
            clear_screen()
            break

        if choice not in directions:
            print(f"\n{RED}Invalid direction, try again!{RESET}\n")
            continue
        
        for _ in range(3):
            for arrow in ["→", "↑", "←", "↑"]:
                print(f"\r{BLUE}The arrow is spinning...{RESET} {arrow}", end="", flush=True)
                time.sleep(0.12) 
        print(f"\r{BLUE}The arrows direction is:{RESET} {arrow_symbols[rdirection]}!      \n")
        
        
        if choice == rdirection:
            print(f"{GREEN}You're right lol! But where will it go now??{RESET}")
        else:
            print(f"{RED}You're so wrong, but where will it go now??{RESET}")
            
        print("-" * 50)  















    
    
        

def save_results(data_list,scan_type):
    if not data_list:
        print(f"\n{RED}[-] No data to save. ")
        time.sleep(4)
        print("\n[*] Continuing ...")
        clear_screen()
        return
    
    choice = input("\n[?] Save results? (Y/n): ").lower()
    if choice == "n":
        clear_screen()
    if choice == "y":
        filename = "tool_report.txt"
        try:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(f"\n=== {scan_type.upper()} REPORT ({time.strftime('%Y-%m-%d %H:%M:%S')}) ===\n")
                for line in data_list:
                    file.write(line + "\n")
            print(f"Saved to {filename}")
        except Exception as e:
            print(f"{RED}[!] Error saving file: {e}{RESET}")

 
        

if __name__ == "__main__":
    clear_screen()
    password()
   
   
    
























#SCRAPPED
"""def flash_password():
    passwords = ["arch123", "puffy3", "dev89", "fBSD1", "SEC99"]
    password = random.choice(passwords)  # take a random password
    
    # salting the password
    salt = os.urandom(16)
    
    # calculating the hash of the password
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 60000)
    # password.encode() = b"puffy3"
    # salt = b'\x8f\xa3...'
    # 60000 = Iterations
    # Result: b'\x1d\x0b\x9c...' (32 Bytes Hash)
    

    print(f"Your password for this session is: {password}")
    time.sleep(0.95)
    clear_screen()
    
    
    return password_hash, salt
    # Returns: (b'\x1d\x0b\x9c...', b'\x8f\xa3...')"""
