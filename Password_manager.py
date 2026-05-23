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

def generate_password():
    chars =string.ascii_letters + string.digits + "@#$%^&*()-+="
    password = "".join(random.choice(chars) for _ in range(8))
    return password

while True:
    print("\n-----PERSONAL PASSWORD MANAGER-----")
    print("1. Save Password")