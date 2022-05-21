import random
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_in_one = list(letters + digits + symbols)


def generate_random_password(number_of_symbols):
    random.shuffle(all_in_one)
    password = random.choices(all_in_one, k=number_of_symbols)
    return("".join(password))


print(f'Your password is: {generate_random_password(8)}')