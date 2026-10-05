projects made by myself in a timespan of 3-6 months



# SHA-256 HASHER

A simple command-line tool that converts any text into its SHA-256 hash.

## Features
- Converts any text input into a **SHA-256 hash**
- Displays both the original text and the resulting hash
- Optionally saves the hash to a file (`hash.txt`)
- Clean, minimal output

## What is SHA-256?
SHA-256 is a cryptographic hash function that turns any input into a **fixed 64-character hex string**. It's:
- **One-way** — you cannot reverse a hash to get the original text
- **Deterministic** — the same input always produces the same hash
- **Collision-resistant** — extremely unlikely for two inputs to produce the same hash

## Usage
terminal:
python3 createHash.py

=============================================================================================================================

# WORD COUNTER

A small utility that counts how often specific words appear in a text file.

## Features
- Count multiple words at once (comma-separated)
- Case-insensitive matching
- Strips punctuation so `Hello!` and `Hello` count the same
- Reports counts per word

## How It Works
1. You enter words to search for
2. You provide a text file
3. The tool reads the file and counts each match

## Usage
terminal:
python3 counting.py

=============================================================================================================================

# PUFFY MULTITOOL

A multi-purpose terminal toolkit for networking, security, and fun — written entirely in Python.

## Features
- Password-protected startup
- NSI-colored terminal UI
- Multi-threaded network operations
- Auto-saves scan results to a report file
- MAC vendor lookup via online API

## Tools Included
| # | Tool | Description |
|---|------|-------------|
| 1 | Port Scanner | Scans common ports and grabs service banners |
| 2 | Network Sweeper | Pings a subnet, resolves MAC + vendor info |
| 3 | IP Geolocation Tracker | Country, region, ISP, proxy info for any IP |
| 4 | Hash Cracker | SHA-256, MD5, SHA-1 and more via wordlist |
| 5 | Username & Password Generator | Secure random credentials |
| 6 | Arrow Prediction Game | Guess where the arrow points next |

## Usage
terminal:
pip install requests
python3 linuxPUFFY.py

## Disclaimer
For **educational and authorized testing only**.


=============================================================================================================================

# MEMORY TEST GAME

A terminal game that challenges you to remember a sequence of random words.

## Features
- 4 difficulty levels: **Easy, Medium, Hard, Hardcore**
- Countdown timer before words disappear
- ANSI color output for clean visuals
- Replay option

## How to Play
1. Choose a difficulty
2. A sequence of words appears for a few seconds
3. The words disappear
4. Type them back in the **exact same order**

## Usage
terminal:
python3 memoryTest.py

## Difficulty
| Level | Words |
|-------|-------|
| Easy      3 
| Medium    5 
| Hard      6 
| Hardcore  9 

=============================================================================================================================

# PASSMAN — CLI PASSWORD MANAGER

A simple, encrypted command-line password manager written in Python.

## Features
- **Master password** protection (SHA-256 hashed, never stored in plaintext)
- **Fernet encryption** (AES-128) for all saved logins
- Add, view, search, and delete logins
- Change master password at any time
- Graceful Ctrl+C handling
- All data stored in `~/.passman/` — **outside the script folder**

## Storage Layout
Everything lives in your home directory

## ⚠️ Name Notice

This project is a personal learning project and is **not affiliated with** any existing software or company named "Passman". The name is a shorthand for "Password Manager" and is not intended to infringe on any trademark. If you own a "Passman" trademark and have concerns, contact me and I'll rename it.
