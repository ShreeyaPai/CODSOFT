import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))
        
        if length < 8:
            print("Password length should be at least 8.")
            return

        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Generated password: {password}")
        
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    main()
