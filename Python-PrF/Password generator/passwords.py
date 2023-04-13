import string
import itertools


def password_generator(length):
    "Creates password containing lowercase letters and digits"
    characters = string.ascii_lowercase + string.digits
    return itertools.product(characters, repeat=length)
