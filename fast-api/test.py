import requests
from time import perf_counter


def test_simple_api(n):
  start_time = perf_counter()
  for x in range(n):
    r = requests.get('http://127.0.0.1:8080/simple-api')
  print(f'----- get char {perf_counter() - start_time} seconds ----')

def test_stock_data(n):
  start_time = perf_counter()
  payload = {'pub_date': '2024-11-01 10:00:00', \
    'headline': 'test', 'content': f'{n}'}
  for x in range(n):
    r = requests.post('http://127.0.0.1:8080/stock_data', params=payload)
  print(f'----- stock data {perf_counter() - start_time} seconds ----')

def test_get_data(n):
  start_time = perf_counter()
  for x in range(n):
    r = requests.get('http://127.0.0.1:8080/fetch_data')
  print(f'----- get data {perf_counter() - start_time} seconds ----')


def test_return_2mb(n):
  start_time = perf_counter()
  for x in range(n):
    r = requests.get('http://127.0.0.1:8080/return_2mb')
  print(f'----- test little file{perf_counter() - start_time} seconds ----')

def test_return_10mb(n):
  start_time = perf_counter()
  for x in range(n):
    r = requests.get('http://127.0.0.1:8080/return_10mb')
  print(f'-----test BIG fille{perf_counter() - start_time} seconds ----')


test_simple_api(1000)
test_stock_data(1000)
test_get_data(1000)
test_return_2mb(1000)
test_return_10mb(1000)
