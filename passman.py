#!/usr/bin/env python3
# ▲ Added to run when opened with a simple launcher script



# launcher script for any terminal on linux  ▼ 

#                    import subprocess
#                    subprocess.Popen(["TERMINALNAME", "-e", "PATH/TO/THE/PASSMAN/SCRIPT"])






import platform 
import sys
from cryptography.fernet import Fernet
import os
import time
import json
import hashlib
import getpass
import signal


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






def ctrl_c_handler(sig, frame):
    #handle ctrl + c without traceback
    sys.exit()

# Register the handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, ctrl_c_handler)









print("ⓅⒶⓈⓈⓈⓂⒶⓃ Password-Manager")
print("'help' for help\n")
time.sleep(2)


HOME = os.path.expanduser("~") # /home/user
PASSMAN_DIR = os.path.join(HOME, ".passman") # /home/user/.passman
os.makedirs(PASSMAN_DIR, exist_ok=True) # create it if its missing





DATA_FILE = os.path.join(PASSMAN_DIR, "passmanpw.json")
KEY_FILE = os.path.join(PASSMAN_DIR, "passmankey.txt")
EPW_FILE = os.path.join(PASSMAN_DIR, "epw.txt")


WRITTENPW = []






def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def masterPassword():
    if os.path.exists(DATA_FILE):
        masterLogin()

    else:
        try:
            print("\nMaster Password not found!")
            while True:
                save_password = input("Create a Master Password ► ")
                if save_password.strip().lower() == "help":
                    helpcentral()
                    continue
                if not save_password.strip():
                    print("Password cannot be empty.")
                    continue
                break
            text_bytes = save_password.encode("utf-8")
            hash_object = hashlib.sha256(text_bytes).hexdigest()


            #calls the save func and the hash to save on the harddrive
            save_user_data(save_password, hash_object)

            print("Master Password saved! Redirecting to Log-in...")
            time.sleep(2)
            clear_screen()
            masterLogin()
        except Exception as e:
            print(f"Error: {e}")






def save_user_data(password, password_hash): #defines the function along with 2 values
    try:
        # could add "password": encrypted! for example but scrapped because of confusion
        data = {"hash": password_hash}
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4) #transforms the dictionary 'data' into JSON-text, writes it into the file 'f' and sets the indent to a comfortable reading format
    except Exception as e:
        print(f"Error: {e}")






def masterLogin():
   while True:
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            stored_data = json.load(file)


            quest = getpass.getpass("Enter your Master Password ► ", stream=None)
            if quest.strip().lower() == "help":
                helpcentral()
                continue
            text_bytes = quest.encode("utf-8")
            input_hash = hashlib.sha256(text_bytes).hexdigest()

            if input_hash != stored_data["hash"]:
                print("Wrong password! Try again.")
                time.sleep(1.1)
                clear_screen()
                continue  
            else:
                print(f"{GREEN}Access Approved...{RESET}")
                time.sleep(1.4)
                clear_screen()
                main()
    except FileNotFoundError:
        print("No password file found. Please set up a password first.")
        time.sleep(2)
        masterPassword()
        return




def main():
    print("Loading personal key")
    time.sleep(1)
    clear_screen()
    # check if file exists and has content
    if os.path.exists(KEY_FILE) and os.path.getsize(KEY_FILE) > 0: 
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
        try:
            Fernet(key)
        except Exception:
            print("\nKey file is corrupted. Regenerating...")
            time.sleep(1.5)
            getKey()
            return

        while True:
                        
                choice = input("1 ► Save new Login\n2 ► Check saved Logins\n\n3 ► Change Master Password\n\nYour choice ► ")
                time.sleep(0.8)
                clear_screen()
                
                if choice == "1":
                    createlogin(key)
                elif choice == "2":
                    showLogins(key)
                elif choice == "3":
                    changeMPW()
                elif choice.strip().lower() == "help":
                    helpcentral()
                    continue
                else:
                    print("Invalid choice, try again!")
                    time.sleep(1.2)
                    clear_screen()
                    continue

    else:
        print("Verification key not available!\nRedirecting...")
        getKey()
        return




def getKey():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    print(f"\nVerification key saved to '{KEY_FILE}'")
    time.sleep(2)
    clear_screen()
    main()
        
    



def createlogin(key):
    WRITTENPW.clear()
    while True:
            source = input("Enter the source that you want to save a Login for: ")
            if source.strip().lower() == "help":
                helpcentral()
                continue
            else:
                put = input("\nEnter the Username and Password that you would like to save: ")
                clear_screen()
                if put.strip().lower() == "help":
                    helpcentral()
                    continue
                if ": " not in put:
                    print("Invalid format! Use: Username: Password")
                    continue
                else:
                        # Step 2: Split the second part on ": "
                        source_parts = put.split(': ')
                        if len(source_parts) == 2:
                            username = source_parts[0].strip()
                            password = source_parts[1].strip()   
                            
                            # Step 3: Rebuild in the new format
                            getData = f"{source} | {username}: {password}"
                            WRITTENPW.append(getData)
                            print(f"Your Input: {getData} ")
                            time.sleep(2)
                            while True:
                                again = input("\nWould you like to save another Login? (y/n): ").lower()
                                if again == "y":
                                    clear_screen()
                                    break
                                elif again == "n":
                                    break
                                elif again.strip().lower() == "help":
                                    helpcentral()
                                    continue
                                else:
                                    print("Invalid choice. Please type 'y', 'n', or 'help' !")
                                    time.sleep(1.5)
                                    continue
                            if again == "y":
                                continue
                            else:
                                break

                        else:
                            print("Invalid format! 'help' for help")
                            time.sleep(1.5)
                            continue
                        
            
                
        

    if not WRITTENPW:
        print("No Logins to save")
        return
    
    while True:
        prompt = "these Logins" if again == "y" else "this Login"
        checking = input(f"\rWould you like to encrypt and save {prompt}? (Y/n): ")
        if checking.strip().lower() == "help":
            helpcentral()
            continue
        elif checking in ["y", ""]:
            break
        elif checking == "n":
            afterCheck = input("\rLogins not saved, would you like to save more? (y/n): ").lower()
            if afterCheck == "y":
                clear_screen()
                createlogin(key)
            if afterCheck.strip().lower() == "help":
                helpcentral()
                continue
            else:
                clear_screen()
                print("No Logins saved. Goodbye!")
                time.sleep(1.2)
                clear_screen()
                sys.exit()
        else:
            print("Invalid input. Type 'y', 'n', or 'help'")
            continue

    
    f = Fernet(key) # Create encryption tool using the secret key
    existing_entries = [] # Reading existing passwords first so it wont overwrite them

    if os.path.exists(EPW_FILE):
        with open(EPW_FILE, "rb") as epw_file:
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

    with open(EPW_FILE, "wb") as epw_file:
        epw_file.write(encrypted_data) # Write encrypted bytes

    WRITTENPW.clear()  
    print("Logins successfully encrypted and saved to epw.txt!")
    time.sleep(2)
    redo = input("Would you like to save another Login? (y/n): ")
    if redo == "y":
        clear_screen()
        createlogin(key)
        return
    elif redo == "n":
        clear_screen()
        main()
    elif redo.strip().lower() == "help":
        helpcentral()
        createlogin(key)
        return
    else:
        clear_screen()
        sys.exit()
    
    

def showLogins(key):

    if not os.path.exists(EPW_FILE):
        print("No saved Logins found")
        time.sleep(2.6)
        clear_screen()
        return 

    try:
        f = Fernet(key)

        with open(EPW_FILE, "rb") as epw_file:
            encrypted_data = epw_file.read()

        
        
        decrypted_bytes = f.decrypt(encrypted_data) # decrypt bytes back to original form
        decrypted_data = decrypted_bytes.decode("utf-8") # convert bytes into a string 

        logins = decrypted_data.split("\n") # Split text into a list by line breaks

        show = "\n".join(logins)
        print("Your saved Logins ▼\n")
        print(show)

        while True:
            print("\n\n----------------------------------------")
            chooseFeature = input("1 ► Search for Logins\n2 ► Delete Logins\n3 ► Return to the menu\n\n► ").strip().lower()
            clear_screen()
            if chooseFeature not in ["1","2","3","help"]:
                print("\nInvalid choice! Try again.")
                time.sleep(1)
                clear_screen()
                continue
            elif chooseFeature == "help":
                helpcentral()
                showLogins(key)
                return



# search 
            elif chooseFeature == "1":
                while True:
                    print(show)
                    search = input("\nSearch for Logins ► ")
                    if search.strip().lower() == "help":
                        helpcentral()
                        continue
                    if search == "":
                        clear_screen()
                        break
                    for login in logins:
                        if search.lower() in login.lower():
                            print(f"Your Login ► {login}")
                            time.sleep(3)
                            clear_screen()
                            print("Your saved Logins ▼\n")
                            print(show)
                            continue
            



#delete
            elif chooseFeature == "2":
                print(show)
                chooseDelete = input("\nEnter the Login that you want to delete ('a' to delete all) \n► ")
                if chooseDelete == "a":
                    if os.path.exists(EPW_FILE):
                        os.remove(EPW_FILE)
                        print(f"All Logins deleted successfully.")
                        time.sleep(1.2)
                        clear_screen()
                        continue
                    else:
                        print(f"No Logins found to delete.")
                        time.sleep(1.2)
                        clear_screen()
                        continue
                
                else:
                    if not os.path.exists(EPW_FILE):
                        print("No File found to delete.")
                        time.sleep(1.2)
                        clear_screen()
                        continue

                    try:
                        f = Fernet(key)

                        # Read and decrypt
                        with open(EPW_FILE, "rb") as file:
                            encrypted_data = file.read()

                        if not encrypted_data:
                            print("No Login found to delete.")
                            time.sleep(1.2)
                            clear_screen()
                            continue


                        decrypted_data = f.decrypt(encrypted_data).decode("utf-8")
                        logins = [line for line in decrypted_data.split("\n") if line.strip()]

                        updated_logins = []
                        deleted_count = 0

                        for login in logins:
                            # login format: "Source | Username: Password"
                            source_part = login.split(" | ")[0].strip()

                            if source_part.lower() == chooseDelete.lower():
                                deleted_count += 1
                                continue
                            updated_logins.append(login)

                        # 3. Check if anything was actually deleted
                        if deleted_count == 0:
                            print(f"No Login found with the source '{chooseDelete}'")
                            time.sleep(1.2)
                            clear_screen()
                            continue

                        # 4. Re-encrypt and save
                        formatted_data = "\n".join(updated_logins)
                        encrypted_data = f.encrypt(formatted_data.encode("utf-8"))

                        with open(EPW_FILE, "wb") as file:
                            file.write(encrypted_data)

                        print(f"Deleted {deleted_count} Login(s) with source '{chooseDelete}'")
                        time.sleep(1.2)
                        clear_screen()

                    except Exception as e:
                        print(f"Error: {e}")
                        time.sleep(1.5)
                        clear_screen()
            


            elif chooseFeature == "3":
                clear_screen()
                return











        

        
            

    except Exception as e:
        print(f"Error {e}")
        #print("Error: Failed to show Logins. Invalid key or corrupted file.")
        time.sleep(2)






def changeMPW():
    while True:
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                stored_data = json.load(file)


                verifying = getpass.getpass("Enter your Master Password to continue: ", stream=None)
                if verifying.strip().lower() == "help":
                    helpcentral()
                    continue
                text_bytes = verifying.encode("utf-8")
                input_hash = hashlib.sha256(text_bytes).hexdigest()

                if input_hash != stored_data["hash"]:
                    print("Wrong password! Try again.")
                    time.sleep(1.1)
                    clear_screen()
                    continue  
                else:
                    print(f"{GREEN}Access Approved...{RESET}")
                    time.sleep(1.4)
                    clear_screen()

                    changing = input("Enter your new Master Password ► ")
                    if changing.strip().lower() == "help":
                        helpcentral()
                        continue
                    if len(changing) <= 6:
                        print("Master Password has to be longer than 6 characters, please try again!")
                        time.sleep(1.5)
                        clear_screen()
                        continue

                    text_bytes = changing.encode("utf-8")
                    hash_object = hashlib.sha256(text_bytes).hexdigest()


                    #calls the save func and the hash to save it
                    save_user_data(changing, hash_object)

                    print("Master Password changed! Redirecting back to the menu")
                    time.sleep(2)
                    clear_screen()
                    main()
        except FileNotFoundError:
            print("Master Password File not found!\nUnaible to continue further.")
            sys.exit()
        








def helpcentral():
    clear_screen()
    print(f"{GREEN}ⓅⒶⓈⓈⓂⒶⓃ  𝖧𝖤𝖫𝖯𝖢𝖤𝖭𝖳𝖤𝖱𝖠𝖫{RESET}\n\n")
    print("Global ▼")
    print("'CTRL + C' to exit ⓅⒶⓈⓈⓂⒶⓃ Password-Manager\n")
    print("Save new Login ▼")
    print("Ideal Source input ► Examplesource")
    print("Ideal Login input ► Exampleuserename: Examplepassword")
    print("\nCheck saved Logins ▼ ")
    print("'a' to delete all Logins")
    print("To delete a Login enter the Source for the Login only (e.g. Firefox)")
    print("'ENTER' to exit")
    print("\nChange Master Password ▼ ")
    print("Changes the overall password for the ⓅⒶⓈⓈⓂⒶⓃ Password-Manager ")

    inp = input("\n\nENTER to continue > ")
    clear_screen()
    





if __name__ == "__main__":
    masterPassword()
    







# "wb" = write binary "rb" = read binary




#
