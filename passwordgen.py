# Import necessary libraries
import random
import string
import time

# Control variable
scriptrunning = True
first_run = False

# Store all generated passwords and emails as tuples (password, email)
password_history = []

# Placeholder function (not used in main flow but kept for style)
def generate_password_old(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase
    pass

# Main program loop
while scriptrunning:

    # Show menu only on restart
    if not first_run:
        print("\n--- Restart Menu ---")
        print("(1) View Password(s) and also email(s) if added")
        print("(2) Continue to generate a new password")
        print("(3) Delete all saved passwords and emails")
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
            # After viewing, go back to menu
            print("Taking you back to the menu...")
            time.sleep(1)
            continue

        elif choice == "2":
            print("Continuing to password generation...")
            time.sleep(1)

        elif choice == "3":
            print("Deleting all saved passwords and emails...")
            password_history.clear()
            print("All saved passwords and emails have been deleted.")
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
            print("Okay, uppercase letters will be used.")
            break
        elif uppercasequestion == 'no':
            use_uppercase = False
            print("Okay, no uppercase letters will be used.")
            break
        else:
            print("Invalid input, please reenter with a valid answer.")

    time.sleep(1)

    # Ask for numbers
    while True:
        numbersquestion = input("Do you want to include numbers? (yes/no): ").lower()
        if numbersquestion == 'yes':
            use_numbers = True
            print("Okay, numbers will be used.")
            break
        elif numbersquestion == 'no':
            use_numbers = False
            print("Okay, no numbers will be used.")
            break
        else:
            print("Invalid input, please reenter with a valid answer.")

    time.sleep(1)

    # Ask for symbols
    while True:
        symbolsquestion = input("Do you want to include symbols? (yes/no): ").lower()
        if symbolsquestion == 'yes':
            use_symbols = True
            print("Okay, symbols will be used.")
            break
        elif symbolsquestion == 'no':
            use_symbols = False
            print("Okay, no symbols will be used.")
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
        password = ''.join(secure_random.choice(characters) for _ in range(length))
        return password

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
        time.sleep(1)
        print("Your password and email have been saved.")
        time.sleep(1)
        password_history.append((password, email_address))
    elif email_choice == "no":
        print("Okay, directing you to the end of the script...")
        time.sleep(1)
        password_history.append((password, None))
    else:
        print("Invalid input, directing you to the end of the script...")
        time.sleep(1)
        password_history.append((password, None))

    # Ask if they want to run the script again
    time.sleep(1)
    print("Thank you for using the Password Generator!")
    restart_script = input("Do you want to re-run the script? {Your Password will additionally be saved} (yes/no): ").lower()

    if restart_script == "no":
        print("Goodbye!, have a great day!")
        time.sleep(1)
        scriptrunning = False
    elif restart_script == "yes":
        first_run = False
        print("Restarting the script...")
        time.sleep(1)
    else:
        print("Invalid input, exiting the script.")
        time.sleep(1)
        scriptrunning = False