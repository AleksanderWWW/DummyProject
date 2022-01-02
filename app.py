import argh

from api.api import get_info


def print_info(number: int = 0) -> None:
    """Function accepts an integer and returns random trivia about the number, fetched from 'numbersapi.com'"""
    get_info(number)


if __name__ == '__main__':
    argh.dispatch_command(print_info)
