import random
import string

def generate_random_password(length=10):
    all_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
print("This is random password generator -",generate_random_password())
