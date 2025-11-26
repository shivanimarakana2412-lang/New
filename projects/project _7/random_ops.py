import random

def random_number():
    """Returns a random number."""
    return random.randint(1, 100)


def random_list():
    """Returns a random list of 3 fruits."""
    items = ["apple", "kiwi", "mango", "banana"]
    return random.sample(items, 3)


def generate_otp():
    """Returns a 6-digit OTP."""
    return "".join(str(random.randint(0, 9)) for _ in range(6))


def random_password():
    """Generates an 8-char password."""
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!@#$%^&*"

    all_chars = letters + letters.upper() + numbers + symbols
    return "".join(random.choice(all_chars) for _ in range(8))
