from fastapi import FastAPI
import psycopg2
from psycopg2 import sql
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Database connection function
def get_db_connection():
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_db_user",
        password="your_db_password",
        host="localhost",
        port="5432"
    )
    return conn

# Endpoint to retrieve data from `test_table`
@app.get("/data")
def read_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT val FROM test_table LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    if result:
        return {"val": result[0]}
    return {"message": "No data found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
