import random
import string

def generate_random_email():
    letters = string.ascii_lowercase
    email = ''.join(random.choice(letters) for i in range(8)) + "@example.com"
    return email

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def generate_random_user():
    return {
        "email": generate_random_email(),
        "password": generate_random_password(),
        "name": ''.join(random.choice(string.ascii_lowercase) for i in range(5))
    }
