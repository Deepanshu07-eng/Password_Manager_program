import random
import string

passwords = {}

#load exiting password file

try:
    with open("passwords.txt", "r") as file:
        for line in file:
            website, password = line.strip().split(":")
            passwords[website]=password

except:
    pass