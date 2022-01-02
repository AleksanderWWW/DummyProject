import argh
from tqdm import tqdm
import json

from api.api import get_info


def print_info(number: int = 0) -> None:
    """Function accepts an integer and returns random trivia about the number, fetched from 'numbersapi.com'"""
    get_info(number)


def info_to_json(out_file_name, *numbers) -> None:
    result = {}

    bar = tqdm(desc="Scraping process", total=len(numbers))
    for number in numbers:
        info = get_info(number)
        result[number] = info
        bar.update(1)
    bar.close()

    print("Writing results to json...", end="")
    with open(out_file_name, "w") as fp:
        json.dump(result, fp)
    print("done")


if __name__ == '__main__':
    # argh.dispatch_command(print_info)
    argh.dispatch_command(info_to_json)
