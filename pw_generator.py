import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    characters = list(string.ascii_lowercase)

    if use_upper:
        characters += list(string.ascii_uppercase)
    if use_digits:
        characters += list(string.digits)
    if use_special:
        characters += list("!@#$%^&*()-_=+")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example use
length = int(input("How long should the password be? "))
password = generate_password(length)
print(f"Your secure password: {password}")
