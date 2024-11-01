import requests
from time import perf_counter


def test_simple_api(n):
    start_time = perf_counter()
    for x in range(n):
        r = requests.get("http://127.0.0.1:5000/char")
    print(f"----- get char {perf_counter() - start_time} seconds ----")


if __name__ == "__main__":
    test_simple_api(1000)
