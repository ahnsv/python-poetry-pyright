from src import __version__
from src.utils import get_random_number, get_random_string

def main():
    print(__version__)
    print(get_random_number(10, 20))
    print(get_random_string())

if __name__ == "__main__":
    main()
