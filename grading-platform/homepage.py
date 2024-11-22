"""
TO RUN:
    flask --app homepage run --debug
"""
from sqlalchemy import create_engine, text
from flask import Flask, request, jsonify, render_template
from markupsafe import escape, Markup

# DB CONFIG
default = True

DIALECT = 'postgresql+psycopg2'
USERNAME = 'postgres' if default else 'michaelchung'
PASSWORD = 'password' if default else 'yay'
HOST = 'localhost'
PORT = 8000
DB_NAME = 'postgres'

# Flask config
app = Flask(__name__)

# Uses given connection to execute given query
def my_query(conn, query):
    return conn.execute(text(query))

@app.route('/')
def do_stuff():
    conn_str = f'{DIALECT}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
    print(f'Connecting to {conn_str}...')

    engine = create_engine(conn_str)

    with engine.connect() as conn:
        result = my_query(conn, """
            SELECT student_name, grade, grade_id
            FROM grades g
            JOIN students s
            ON g.student_id = s.student_id
        """)

        conn.commit()

        return render_template('home.html', results=result.all())

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        print(request.view_args)
    return jsonify({'result': 'hi'})