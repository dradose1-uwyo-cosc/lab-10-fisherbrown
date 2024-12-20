# Fisher Brown
# UWYO COSC 1010
# 19 Nov 24
# Lab 10
# Lab Section: 10
# Sources, people worked with, help given to: Jayden Robison
# your
# comments
# here

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-else block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.

from pathlib import Path
way = Path('hash')
path = Path('rockyou.txt')
try:
    contents1 = path.read_text()
except FileNotFoundError:
    print(f'{path} not found')
else:
    lines = contents1.splitlines() 
try:
    contents2 = way.read_text()
except FileNotFoundError:
    print(f'{way} not found')
else:
    code = contents2

for line in lines:
    if get_hash(line) == code:
        print(f'The password is {line}')
        break
    else: 
        continue
        
