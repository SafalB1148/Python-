import re

def check_password_strength(password):
    min_length = 8
    max_length = 16
    has_uppercase_letters = r'[A-Z]'
    has_lowercase_letters = r'[a-z]'
    has_digits = r'\d'
    has_special_characters = r'[@$!%*?&]'

    if len(password) < min_length or len(password) > max_length:
        return "Password must be between 8 to 16 characters long."
    if not re.search('[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    if not re.search('[a-z]', password):
        return "Password must contain at least one lowercase letter."
    if not re.search(has_digits, password):
        return "Password must contain at least one digit."
    if not re.search(has_special_characters, password):
        return "Password must contain at least one special character."
    return "Password is strong"

while True:
    password = input("Enter a password: ")
    result = check_password_strength(password)
    if result != "Password is strong":
        print(result)
    else:
        print(result)
        print("Password is strong! You can proceed.")
        break