import random
import string

def generate_password(length):
    #including ASCII, digits and punctuations all together for a safer password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to Password Generator")
    try:
        length = int(input("How long would you like your password to be? "))
        if length < 1:
            print("Please enter a positive integer")
        else:
            password = generate_password(length)
            print(f"Your Password is: {password}")
    except ValueError:
            print("Please enter a positive integer")

if __name__ == "__main__":
    main()
