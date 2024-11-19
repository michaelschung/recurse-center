from sqlalchemy import create_engine, text
from flask import Flask

default = True

DIALECT = 'postgresql+psycopg2'
USERNAME = 'postgres' if default else 'michaelchung'
PASSWORD = 'password' if default else 'yay'
HOST = 'localhost'
PORT = 8000
DB_NAME = 'postgres'

app = Flask(__name__)

def my_query(conn, query):
    return conn.execute(text(query))

@app.route("/")
def do_stuff():
    conn_str = f'{DIALECT}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
    print(f'Connecting to {conn_str}...')

    engine = create_engine(conn_str)

    with engine.connect() as conn:
        result = my_query(conn, """DROP TABLE IF EXISTS test_table""")

        result = my_query(conn, """
            CREATE TABLE IF NOT EXISTS test_table (
                id SERIAL PRIMARY KEY,
                key INT,
                val VARCHAR(255)
            )
        """)

        result = my_query(conn, """
            INSERT INTO test_table (key, val) VALUES
                (10, 'Hello'),
                (20, 'Goodbye')
        """)

        result = my_query(conn, """
            SELECT *
            FROM test_table
            WHERE key < 40
        """)

        print(result.all())

        result = my_query(conn, """
            INSERT INTO test_table (key, val) VALUES
                (30, 'YO')
        """)

        result = my_query(conn, """
            SELECT *
            FROM test_table
            WHERE key < 40
        """)

        # result = my_query(conn, """SELECT * FROM test_table""")
        # print(result.all())

        conn.commit()

        return str(result.all())