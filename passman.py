#!/usr/bin/env python3

# pswd manager

# what to add: , master pw, search for pw


import sys
from cryptography.fernet import Fernet
import os
import time

print("ⓅⒶⓈⓈⓈⓂⒶⓃ Password-Manager")
print("'help' for help")
WRITTENPW = []




def main():
    time.sleep(1.6)
    os.system("clear")
    print("Loading key to verify ...")
    time.sleep(1.4)
    if os.path.exists("passmankey.txt"): 
        with open("passmankey.txt", "rb") as key_file:
            key = key_file.read()
            while True:
                try:
                            
                    choice = input("1: Save new Login | 2: Check saved Logins > ")
                    if choice == "1":
                        pwds(key)
                    elif choice == "2":
                        showPwds(key)
                    elif choice == "help":
                        helpcentral()
                    else:
                        print("Invalid choice, try again!")
                        time.sleep(1.7)
                        os.system('clear')
                        continue
                except KeyboardInterrupt:
                    os.system('clear')
                    break

    else:
        print("Key not available!\nRedirecting...")
        getKey()




def getKey():
    key = Fernet.generate_key()
    with open("passmankey.txt", "wb") as key_file:
        key_file.write(key)
        print("\nKey saved to passmankey.txt")
        time.sleep(2)
        os.system('clear')
        pwds(key)
    



def pwds(key):
    time.sleep(1.6)
    while True:
        try:
            put = input("Enter the Username, Source and Password that you would like to save: ")
            if put == "help":
                helpcentral()
                continue
            if ": " not in put or " | " not in put:
                print("Invalid format! Use: Username | Source: Password")
                continue
            else:
                parts = put.split(' | ')
                if len(parts) == 2:
                    username = parts[0].strip()
                    source_password = parts[1]
                    
                    # Step 2: Split the second part on ": "
                    source_parts = source_password.split(': ')
                    if len(source_parts) == 2:
                        source = source_parts[0].strip()
                        password = source_parts[1].strip()
                        
                        # Step 3: Rebuild in the new format
                        getData = f"{username} | {source}: {password}"
                        WRITTENPW.append(getData)
                        print(f"Your Input: {getData} ")
                        time.sleep(2)
                        while True:
                            again = input("Would you like to save another Login? (y/n): ").lower()
                            if again == "y":
                                os.system('clear')
                                break
                            elif again == "n":
                                break
                            elif again == "help":
                                helpcentral()
                            else:
                                print("Invalid choice. Please type 'y', 'n', or 'help' !")
                                time.sleep(1.5)
                                continue
                        if again == "y":
                            continue
                        else:
                            break

                    else:
                        print("Invalid format! Use: Username | Source: Password")
                        time.sleep(1.5)
                        continue
                        
            
                
        except KeyboardInterrupt:
            os.system('clear')
            print("Goodbye!")
            sys.exit()

    if not WRITTENPW:
        print("No Logins to save")
        return
    
    while True:
        checking = input(f"Would you like to encrypt save these Logins in the file 'epw.txt'? (Y/n): ")
        if checking == "help":
            helpcentral()
            continue
        elif checking in ["y", ""]:
            break
        elif checking == "n":
            print("Logins not saved. Goodbye!")
            sys.exit()
        else:
            print("Invalid input. Type 'y', 'n', or 'help'")
            continue

    
    f = Fernet(key) # Create encryption tool using the secret key
    existing_entries = [] # Reading existing passwords first so it wont overwrite them

    if os.path.exists("epw.txt"):
        with open("epw.txt", "rb") as epw_file:
            old_encrypted = epw_file.read()
            if old_encrypted:
                old_decrypted = f.decrypt(
                    old_encrypted
                ).decode("utf-8")
                existing_entries = [item for item in old_decrypted.split("\n") if item.strip()
                ]

#combine all passwords with the new ones
    all_passwords = existing_entries + WRITTENPW
    formatted_data = "\n".join(all_passwords)
    encrypted_data = f.encrypt(
        formatted_data.encode("utf-8")
    )# Split text into a list by line breaks

    with open("epw.txt", "wb") as epw_file:
        epw_file.write(encrypted_data) # Write encrypted bytes

    WRITTENPW.clear()  
    print("Logins successfully encrypted and saved to epw.txt!")
    time.sleep(2)
    redo = input("Would you like to save another Login? (y/n): ")
    if redo == "y":
        pass
    if redo == "help":
        helpcentral()
    else:
        os.system("clear")
        sys.exit()
    
    

def showPwds(key):
    print("-Your saved Logins-\n")

    if not os.path.exists("epw.txt"):
        print("No saved Logins found (epw.txt missing).")
        time.sleep(2)
        return

    try:
        f = Fernet(key)

        with open("epw.txt", "rb") as epw_file:
            encrypted_data = epw_file.read()

        
        
        decrypted_bytes = f.decrypt(encrypted_data) # decrypt bytes back to original form
        decrypted_data = decrypted_bytes.decode("utf-8") # convert bytes into a string 

        passwords = decrypted_data.split("\n") # Split text into a list by line breaks

        show = "\n".join(passwords)
        
        print(show)


        input("\nPress Enter to return...")
        os.system("clear")

    except Exception as e:
        print("Error: Failed to Logins. Invalid key or corrupted file.")
        time.sleep(2)



def helpcentral():
    os.system('clear')
    print("'CTRL + C' to quit")
    print("Ideal input ->  Exampleusername | Examplesourcename: Examplepassword")
    print("key-file has to be in the same folder as ⓅⒶⓈⓈⓂⒶⓃ Password-Manager ")

    i = input("\nENTER to continue > ")
    os.system('clear')
    





if __name__ == "__main__":
    main()
    







# "wb" = write binary "rb" = read binary




#
"""┌─────────────────────────────────────────────
│                    PASSMAN Password-Manager                     │
│                                                                 │
│  1. START                                                      │
│  2. Check for key file (passmankey.txt)                       │
│     ├── Exists → Load key → Show menu                         │
│     └── Missing → Generate new key                            │
│                                                                 │
│  3. MENU (1: Save Login | 2: View Logins)                     │
│     ├── 1: pwds()                                             │
│     │   ├── Collect Logins (while loop)                      │
│     │   │   ├── Format: Username | Source: Password          │
│     │   │   ├── Validate input                               │
│     │   │   ├── Append to new_passwords                     │
│     │   │   └── Ask: "Another? (y/n)"                      │
│     │   │       ├── y → Continue collecting                 │
│     │   │       └── n → Proceed to save                    │
│     │   ├── Encrypt and save to epw.txt                     │
│     │   └── Ask: "Save another? (y/n)"                     │
│     │       ├── y → Back to menu                            │
│     │       └── n → Exit                                   │
│     │                                                        │
│     └── 2: showPwds()                                       │
│         ├── Decrypt epw.txt                                 │
│         ├── Display all Logins                              │
│         └── Press Enter to return                          │
│                                                                 │
│  4. EXIT                                                      │
└─────────────────────────────────────────────────────────────────┘"""