import argh
from tqdm import tqdm
import msgpack
from pathlib import Path
import os

from api.api import get_info


def print_info(number: int = 0) -> None:
    """Function accepts an integer and returns random trivia about the number, fetched from 'numbersapi.com'"""
    print(get_info(number))


def info_to_binary(out_file_name: str, *numbers: int) -> None:
    result: dict = {}

    bar = tqdm(desc="Scraping process", total=len(numbers))
    for number in numbers:
        info = get_info(number)
        result[number] = info
        bar.update(1)
    bar.close()

    print("Writing results to msgpack...", end="")
    save_path = Path(os.getcwd(), "output", out_file_name)
    with open(save_path, "wb") as fp:
        fp.write(msgpack.packb(result))
    print("done")


if __name__ == '__main__':
    argh.dispatch_commands([print_info, info_to_binary])
