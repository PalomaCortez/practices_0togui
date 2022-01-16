## Cap 6 - functions
#EX4 - Random Character

from random import randint

# Generate a random character between ch1 and ch2
def get_random_character(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))

#Generate a random lowercase letter
def get_random_lowercase_letter():
    return get_random_character('a', 'z')

# Generate a random uppercase letter
def get_random_uppercase_letter():
    return get_random_character('A', 'Z')

# Generate a random digit character
def get_random_digit_character():
    return get_random_character('0', '9')

# Generate a random character
def get_random_ascii_character():
    return chr(randint(0, 127))