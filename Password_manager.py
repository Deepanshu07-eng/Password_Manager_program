import json
import random
import string

FILE_NAME = "passwords.json"


# Load passwords from JSON file
def load_passwords():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}

    except json.JSONDecodeError:
        print("Error: Password file is corrupted.")
        return {}

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return {}


# Save passwords to JSON file
def save_passwords(passwords):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(passwords, file, indent=4)

    except Exception as e:
        print(f"Error saving passwords: {e}")


# Get website input
def get_website():
    return input("Enter website name: ").strip().lower()


# Get password input
def get_password():
    return input("Enter password: ").strip()


# Generate strong password
def generate_password():

    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length should be at least 4.")
            return None

    except ValueError:
        print("Please enter a valid number.")
        return None

    letters = string.ascii_letters
    digits = string.digits
    symbols = "@#$%&*!?"

    password = []

    for _ in range(length):

        choice = random.choice(["letter", "digit", "symbol"])

        if choice == "letter":
            password.append(random.choice(letters))

        elif choice == "digit":
            password.append(random.choice(digits))

        else:
            password.append(random.choice(symbols))

    random.shuffle(password)

    return "".join(password)


# Add password
def add_password(passwords):

    site = get_website()
    pwd = get_password()

    passwords[site] = pwd

    save_passwords(passwords)

    print("Password Saved Successfully.")


# View passwords
def view_passwords(passwords):

    if not passwords:
        print("No passwords saved.")
        return

    print("\n===== SAVED PASSWORDS =====")

    for site, pwd in passwords.items():
        print(f"{site} : {pwd}")


# Search password
def search_password(passwords):

    if not passwords:
        print("No passwords available.")
        return

    site = get_website()

    if site in passwords:
        print("Password:", passwords[site])

    else:
        print("Website not found.")


# Update password
def update_password(passwords):

    if not passwords:
        print("No passwords available.")
        return

    site = get_website()

    if site in passwords:

        new_pwd = get_password()

        passwords[site] = new_pwd

        save_passwords(passwords)

        print("Password Updated Successfully.")

    else:
        print("Website not found.")


# Delete password
def delete_password(passwords):

    if not passwords:
        print("No passwords available.")
        return

    site = get_website()

    if site in passwords:

        del passwords[site]

        save_passwords(passwords)

        print("Password Deleted Successfully.")

    else:
        print("Website not found.")


# Main Program
def main():

    passwords = load_passwords()

    while True:

        print("\n===== PASSWORD MANAGER =====")
        print("1. Add New Password")
        print("2. View Passwords")
        print("3. Generate Password")
        print("4. Search Password")
        print("5. Update Password")
        print("6. Delete Password")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        match choice:

            case "1":
                add_password(passwords)

            case "2":
                view_passwords(passwords)

            case "3":

                password = generate_password()

                if password:
                    print("Generated Password:", password)

            case "4":
                search_password(passwords)

            case "5":
                update_password(passwords)

            case "6":
                delete_password(passwords)

            case "7":
                print("Good Bye...")
                break

            case _:
                print("Invalid Choice. Try Again.")


if __name__ == "__main__":
    main()