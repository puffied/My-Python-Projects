import sys 
import os
import time
import platform




def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    

def info():
    ses = platform.system()
    print(f"Your current session is on {ses}")
    print("\n=Read=\n-- Enter words separated by commas (e.g. test,print,hello)\n-- Make sure the file that you use is in the folder of this tool.\nMake sure the file that you use is in the folder of this tool.")
    choice = input("\nWould you like to continue? (y/n): ").lower()
    if choice != "y":
        print("Goodbye!")
        time.sleep(1.6)
        clear()
    else:
        clear()
        cwrds()





def cwrds():
   
    while True:
        try:
            user_input = input("Enter the words, that you would like to count: ")

            search_words = [word.strip() for word in user_input.split(',') if word.strip()] # out of "water, print, lower" becomes: ["water", "print", "lower"] and search word is a word stripped out of the list (with the help of: for word in ......)

            word_counts = {word: 0 for word in search_words} # dictionary to count each word | looks like: {"water": 0, "print": 0, "lower": 0}

            clear()
            path = input("Enter the name of your file: ")

          
        

            with open(path, 'r') as file: 
                for line in file: #returns lines
                    for word in line.split(): # splits every line into words
                        word_clean = word.strip('.,!?;:"()[]') # set so Hello! and Hello will seen as the same
                        for search_word in search_words:
                            if word_clean == search_word:
                                word_counts[search_word] += 1
                        
                        
            print(f"\nResults:")
            
            for search_word in search_words:
                count = word_counts[search_word]
                print(f"'{search_word}': {count} times")

                
                    

                    
            choice2 = input("\nWould you like to count again? (y/n): ").lower()
            if choice2 == "y":
                
                continue
            else:
                print("Goodbye!")
                sys.exit(0)

        except FileNotFoundError:
            print(f"Error: File '{path}' was not found!")
            retry = input("Try again? (y/n): ").lower()
            if retry == "y":
                continue
            else:
                sys.exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(2)

                
if __name__ == "__main__":
    info()