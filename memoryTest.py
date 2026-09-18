import random 
import time
import os
import sys
import platform



GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


randomWords = [
"kernel",
"bash",
"sudo",
"terminal",
"ubuntu",
"debian",
"arch",
"grep",
"sed",
"system",
"root",
"daemon",
"cron",
"top",
"htop",
"log",
"files",
"node",
"grub",
"init",
"shell",
"out",
"in",
"sys",
"pipe",
"alias",
"link",
"manage",
"distro",
"pacman",
"yum",
"ball",
"zip",
"sync",
"fstab",
"swap",
"mount",
"umount",
"port",
"ip",
"firewall",
"groups",
"lip",
"apple",
"river",
"mountain",
"whisper",
"shadow",
"journey",
"window",
"silence",
"feather",
"ocean",
"candle",
"harbor",
"pancake",
"breeze",
"lantern",
"velvet",
"puzzle",
"compass",
"meadow",
"echo",
"sunset",
"blanket",
"thunder",
"sculpture",
"coffee",
"guitar",
"orbit",
"pebble",
"starlight",
"forest",
"mirage",
"canvas",
"bridge",
"harvest",
"drizzle",
"marathon",
"pyramid",
"telescope",
"harmonica",
"blossom",
"fossil",
"glacier",
"compass",
"porch",
"bison",
"horizon",
"avalanche",
"tulip",
"fountain",
"orchard", ]


def countdown():
   # uchoice = int(input("Enter how many seconds you need (7 is the max): "))
    for num in range(1, 5): #uchoice
        sys.stdout.write(f"\rGet ready! {num}")
        sys.stdout.flush()
        time.sleep(1)
        

            

def clear_screen():
    if platform.system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def wordGen():
    while True:
        try:
            choice = int(input("Select the difficulty that you would like to play on ►  1 = Easy | 2 = Medium | 3 = Hard | 4 = Hardcore: "))

            if choice == 1:
                selected_words = random.sample(randomWords, 3)
                clear_screen()
            elif choice == 2:
                selected_words = random.sample(randomWords, 5)
                clear_screen()
            elif choice == 3:
                selected_words = random.sample(randomWords, 6)
                clear_screen()
            elif choice == 4:
                selected_words = random.sample(randomWords, 9)
                clear_screen()
            else:
                print("Invalid choice! Try again.")
                time.sleep(1.1)
                clear_screen()
                continue


            result = " ".join(selected_words)
            print(f"{CYAN}Your words ►{RESET}    {result}    ")
            countdown()
            clear_screen()
            
            print("Enter the words in the correct order  ")
            query = input("►   ")
            if query == result:
                print(f"\n{GREEN}You won!\nGreat Memory :D{RESET}")
                repeat = input("\nWould you like to play again? (Y/n): ").lower()
                if repeat == "y":
                    clear_screen()
                    continue
                if repeat == "n":
                    print("Goodbye!")
                    time.sleep(1.4)
                    clear_screen()
                    sys.exit()
                else:
                    print("Invalid choice! Exiting.")
                    time.sleep(1.4)
                    clear_screen()
                    sys.exit()
        
        
            else:
                print(f"\n{RED}You lost!\nGotta work on your memory ;P{RESET}")
                time.sleep(1.1)
                print(f"\nThese were the words ►  {result} \n")
                time.sleep(1.1)
                repeat = input("\nWould you like to play again? (Y/n):").lower()
                if repeat == "y":
                    clear_screen()
                    continue
                if repeat == "n":
                    print("Goodbye!")
                    time.sleep(1.4)
                    clear_screen()
                    sys.exit()
                else:
                    print("Invalid choice! Exiting.")
                    time.sleep(1.4)
                    clear_screen()
                    sys.exit()


                    


                

        except ValueError:
            print("Please enter a valid number!")
            continue
                
                    
                        


if __name__ == "__main__":
    print(f"{YELLOW}Random word Memory tester{RESET}\n")
    wordGen()
        


