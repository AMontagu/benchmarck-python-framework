import uvicorn
import sqlite3

from fastapi import FastAPI, HTTPException
from fastapi.responses import Response, FileResponse
from pydantic import BaseModel, constr, validator
from datetime import datetime

datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

app = FastAPI()

DB_NAME = 'fastApiPost.db'
TABLE_NAME = 'Post'

file_path_2mb = './data/generated_file_2MB.json'
file_path_10mb = './data/generated_file_10MB.json'



sql_statements = f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            pub_date DATE,
            headline VARCHAR(200),
            content TEXT );"""

def create_db():
  try:
    with sqlite3.connect("fastApiPost.db") as conn:
        print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
  except sqlite3.OperationalError as e:
        print("Failed to open database:", e)

def create_table(db_name: str)-> None:
  con = sqlite3.connect(f"{db_name}")
  cur = con.cursor()
  cur.execute(f"{sql_statements}")
  con.close()


def write_table(db_name: str, table_name: str, pub_date: datetime, \
  headline: str, content: str)-> None:
  con = sqlite3.connect(f"{db_name}")
  cur = con.cursor()
  datetime.now()
  cur.execute(f"""
    INSERT INTO {table_name} VALUES
        ('{pub_date}','{headline}','{content}' )""")
  con.commit()
  con.close()

def fetch_data(db_name: str, table_name: str)-> None :
  con = sqlite3.connect(f"{db_name}")
  cur = con.cursor()
  res = cur.execute(f"""
    SELECT * FROM {table_name}""")
  data = res.fetchall()
  con.close()
  return data



@app.get('/simple-api')
def simple_api():
  return Response('b')


@app.post('/stock_data')
def stock_data(pub_date,headline,content)-> None:
  write_table(DB_NAME, TABLE_NAME, pub_date,headline,content)
  return Response('Inserted in db', status_code=200)


@app.get('/fetch_data')
def get_data()-> None:
  data = fetch_data(DB_NAME, TABLE_NAME)
  return Response(f'Data fetched: {data}', status_code=200)


@app.get('/return_2mb')
async def return_2mb():
  return FileResponse(file_path_2mb)

@app.get('/return_10mb')
async def return_10mb():
  return FileResponse(file_path_10mb)

if __name__ == "__main__":
    create_db()
    create_table(DB_NAME)
    uvicorn.run("app:app", host="0.0.0.0", port=8080, log_level="info")
