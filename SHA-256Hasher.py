import hashlib
import os

def generate_sha256():
    text_input = input("Enter text to convert into a hash: ")
    encoded_bytes = text_input.encode('utf-8') #string into bytes utf8 required by hashlib
    hash_object = hashlib.sha256(encoded_bytes) #passes the bytes into SHA-256 algorythm
    hex_hash = hash_object.hexdigest()

    print("\n--- Result ---")
    print(f"Original Text : {text_input}")
    print(f"SHA-256 Hash  : {hex_hash}")

    choice = input("\nWould you like to save the generated hash in a file? (Y/n) ").lower()
    if choice == "y":
        with open("hash.txt", "w") as file:
            file.write(f"{hex_hash}") 
        print("Hash was saved in 'hash.txt'.")
    elif choice in ["n", "e"]:
        print("Goodbye.")
    else:
        print("Invalid choice, exiting the tool.")


if __name__ == "__main__":
    generate_sha256()