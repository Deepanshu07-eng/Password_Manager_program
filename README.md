# Password Manager

A command-line based Password Manager built with Python that allows users to securely manage website passwords. The application supports adding, viewing, searching, updating, deleting, and generating strong passwords while storing data persistently using a JSON file.

## Features

* Add new website passwords
* View all saved passwords
* Search passwords by website name
* Update existing passwords
* Delete saved passwords
* Generate strong random passwords with custom length
* Case-insensitive website search
* Persistent storage using JSON
* Exception handling for file operations and invalid inputs
* Modular and reusable code structure

## Technologies Used

* Python
* JSON
* File Handling
* Random Module
* String Module

## Project Structure

```text
Password_Manager/
│
├── password_manager.py
├── passwords.json
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/password-manager.git
```

2. Navigate to the project folder

```bash
cd password-manager
```

3. Run the program

```bash
python password_manager.py
```

## Menu Options

```text
1. Add New Password
2. View Passwords
3. Generate Password
4. Search Password
5. Update Password
6. Delete Password
7. Exit
```

## How It Works

* Passwords are stored in a local JSON file.
* Website names are automatically converted to lowercase for consistent searching.
* Users can generate passwords of custom lengths.
* Password data is automatically loaded when the program starts.
* Any changes made are instantly saved to the JSON file.

## Future Improvements

* Master Password Authentication
* Password Encryption
* Password Strength Checker
* Export and Backup Functionality
* Graphical User Interface (GUI)
* Password Categories and Tags

## Learning Outcomes

This project helped in understanding:

* Python Functions
* Dictionaries
* JSON Handling
* File Operations
* Exception Handling
* Modular Programming
* Random Password Generation
* Data Persistence

## Author

Deepanshu

Python CLI Project for learning file handling, JSON storage, and password management concepts.
