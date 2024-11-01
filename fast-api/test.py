import requests
import time


def test_simple_api(n):
  start_time = time.time()
  for x in range(n):
    r = requests.get('http://127.0.0.1:5000/simple-api')
    r.status_code
  print(f'-----{time.time() - start_time} seconds ----')

def test_stock_data(n):
  start_time = time.time()
  payload = {'pub_date': '2024-11-01 10:00:00', \
    'headline': 'test', 'content': f'{n}'}
  for x in range(n):
    r = requests.post('http://127.0.0.1:5000/stock_data', params=payload)
    r.status_code
  print(f'-----{time.time() - start_time} seconds ----')

def test_get_data(n):
  start_time = time.time()
  for x in range(n):
    r = requests.get('http://127.0.0.1:5000/fetch_data')
    r.status_code
  print(f'-----{time.time() - start_time} seconds ----')


def test_return_2mb(n):
  start_time = time.time()
  for x in range(n):
    r = requests.get('http://127.0.0.1:5000/return_2mb')
    r.status_code
  print(f'-----{time.time() - start_time} seconds ----')

def test_return_10mb(n):
  start_time = time.time()
  for x in range(n):
    r = requests.get('http://127.0.0.1:5000/return_10mb')
    r.status_code
  print(f'-----{time.time() - start_time} seconds ----')
