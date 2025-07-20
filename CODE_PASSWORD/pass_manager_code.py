import random
import string

def generate_password(length=12, use_special_chars=True):
    charecters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(charecters, k=length))
    return password
print("Generated Password: ", generate_password())