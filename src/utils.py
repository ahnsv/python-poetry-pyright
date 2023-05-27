import random
import string


def get_random_number(start: int, end: int) -> int:
    return random.randrange(start=start, stop=end)

# get a random string of length 10
def get_random_string() -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

