import random
import string

passwords = {}

# Load existing passwords
try:
    with open("password.txt", "r") as file:
        for line in file:
            website, password = line.strip().split(":")
            passwords[website] = password
except:
    pass


# Generate password
def generate_password():
    chars = string.ascii_letters + string.digits + "@#$%"
    password = "".join(random.choice(chars) for i in range(10))
    return password


# Save passwords to file
def save_file():
    with open("password.txt", "w") as file:
        for website, password in passwords.items():
            file.write(f"{website}:{password}\n")


while True:

    print("\n===== PASSWORD MANAGER =====")
    print("1. Add New Password")
    print("2. View Passwords")
    print("3. Generate Password")
    print("4. Search Password")
    print("5. Update Password")
    print("6. Delete Password")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Save Password
    if choice == "1":

        site = input("Enter website: ")
        pwd = input("Enter password: ")

        passwords[site] = pwd
        save_file()

        print("Password Saved Successfully")

    # View Passwords
    elif choice == "2":

        if not passwords:
            print("No passwords saved")

        else:
            print("\nSaved Passwords:")

            for site, pwd in passwords.items():
                print(site, ":", pwd)

    # Generate Password
    elif choice == "3":

        print("Generated Password:", generate_password())

    # Search Password
    elif choice == "4":

        site = input("Enter website name: ")

        if site in passwords:
            print("Password:", passwords[site])

        else:
            print("Website not found")

    # Update Password
    elif choice == "5":

        site = input("Enter website name: ")

        if site in passwords:

            new_pwd = input("Enter new password: ")

            passwords[site] = new_pwd
            save_file()

            print("Password Updated Successfully")

        else:
            print("Website not found")

    # Delete Password
    elif choice == "6":

        site = input("Enter website name: ")

        if site in passwords:

            del passwords[site]
            save_file()

            print("Password Deleted Successfully")

        else:
            print("Website not found")

    # Exit
    elif choice == "7":

        print("Good Bye...")
        break

    else:
        print("Invalid Input")