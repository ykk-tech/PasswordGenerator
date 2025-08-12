# Import necessary libraries
import random
import string
import time
import os

# My Main Function tee hee
def mygithub():
    print("This script was created by @ykk-tech on GitHub <3")

# File to store saved passwords
SAVE_FILE = "saved_passwords.txt"

# Control variables
scriptrunning = True
first_run = True

# Store all generated passwords and emails as tuples (password, email)
password_history = []

# =================
# Helper functions
# =================
def load_passwords():
    """Load saved passwords and emails from file into memory."""
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(" | Email: ")
                    pw = parts[0].replace("Password: ", "")
                    email = parts[1] if len(parts) > 1 and parts[1] != "None" else None
                    password_history.append((pw, email))

def save_password(password, email):
    """Append password and email to file."""
    with open(SAVE_FILE, "a") as f:
        f.write(f"Password: {password} | Email: {email}\n")

def clear_saved_passwords():
    """Clear the file and memory list."""
    open(SAVE_FILE, "w").close()  # overwrite with empty
    password_history.clear()

# Load existing passwords at startup
load_passwords()

# Placeholder function (kept for style)
def generate_password_old(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase
    pass

# =================
# Main program loop
# =================
while scriptrunning:

    # Show menu only on restart
    if not first_run:
        print("\n--- Restart Menu ---")
        print("(1) View Password(s) and also email(s) if added")
        print("(2) Continue to generate a new password")
        print("(3) Delete all saved passwords and emails")
        print("(4) Check out my GitHub")
        choice = input("Enter your choice: ")

        if choice == "1":
            if password_history:
                print("\nPreviously generated credentials:")
                for i, entry in enumerate(password_history, 1):
                    pw, email_addr = entry
                    if email_addr:
                        print(f"{i}. Password: {pw} | Email: {email_addr}")
                    else:
                        print(f"{i}. Password: {pw}")
            else:
                print("\nNo passwords have been generated yet.")
            print("Taking you back to the menu...")
            time.sleep(1)
            continue

        elif choice == "2":
            print("Continuing to password generation...")
            time.sleep(1)

        elif choice == "3":
            print("Deleting all saved passwords and emails...")
            clear_saved_passwords()
            time.sleep(1)
            print("All saved passwords and emails have been deleted.")
            time.sleep(1)
            continue

        elif choice == "4":
            mygithub()
            time.sleep(2)
            print("Taking you back to the menu...")
            time.sleep(1)
            continue

        else:
            print("Invalid choice, please try again.")
            time.sleep(1)
            continue

    print("\nWelcome to the Password Generator!")
    time.sleep(1)
    print("This script will help you generate a secure password.")
    time.sleep(1)

    # Length of the password
    while True:
        input_length = int(input("Enter how many characters total you want in your password: "))
        if input_length < 1:
            print("Please enter a number greater than 0.")
        else:
            length = input_length
            print(f"Okay, your password will be {length} characters long.")
            time.sleep(1)
            break

    # Ask for uppercase letters
    while True:
        uppercasequestion = input("Do you want to include uppercase letters? (yes/no): ").lower()
        if uppercasequestion == 'yes':
            use_uppercase = True
            break
        elif uppercasequestion == 'no':
            use_uppercase = False
            break
        else:
            print("Invalid input, please reenter with a valid answer.")

    time.sleep(1)

    # Ask for numbers
    while True:
        numbersquestion = input("Do you want to include numbers? (yes/no): ").lower()
        if numbersquestion == 'yes':
            use_numbers = True
            break
        elif numbersquestion == 'no':
            use_numbers = False
            break
        else:
            print("Invalid input, please reenter with a valid answer.")

    time.sleep(1)

    # Ask for symbols
    while True:
        symbolsquestion = input("Do you want to include symbols? (yes/no): ").lower()
        if symbolsquestion == 'yes':
            use_symbols = True
            break
        elif symbolsquestion == 'no':
            use_symbols = False
            break
        else:
            print("Invalid input, please reenter with a valid answer.")

    # Build the character set based on user input
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Generate the password
    time.sleep(1)
    print("Generating your password...")
    time.sleep(1)
    secure_random = random.SystemRandom()

    def generate_password(length, characters):
        return ''.join(secure_random.choice(characters) for _ in range(length))

    password = generate_password(length, characters)

    # Ask to add email
    print("Generated! One second please...")
    time.sleep(1)
    print(f"Your secure password is: {password}")
    time.sleep(1)
    email_choice = input("Do you want to add an email to your password? (yes/no): ").lower()

    if email_choice == "yes":
        email_address = input("Please enter your email address: ")
        print(f"Your password with email is: {password} | Email: {email_address}")
        password_history.append((password, email_address))
        save_password(password, email_address)
    else:
        password_history.append((password, None))
        save_password(password, None)

    time.sleep(1)

    # Ask if they want to run the script again
    print("Thank you for using the Password Generator!")
    restart_script = input("Do you want to re-run the script? (yes/no): ").lower()

    if restart_script == "no":
        print("Goodbye!, have a great day!")
        scriptrunning = False
    elif restart_script == "yes":
        first_run = False
        print("Restarting the script...")
        time.sleep(1)
    else:
        print("Invalid input, exiting the script.")
        scriptrunning = False
