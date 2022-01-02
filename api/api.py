import requests

from .settings import API_URL


def get_info(number: int) -> str:
    url = API_URL + str(number)

    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else:
        print("An error occurred, code={}".format(r.status_code))
        return ""


