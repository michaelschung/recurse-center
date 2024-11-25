"""
TO RUN:
    flask --app homepage run --debug
"""
from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape, Markup

# DB config
default = True
DIALECT = 'postgresql+psycopg2'
USERNAME = 'postgres' if default else 'michaelchung'
PASSWORD = 'password' if default else 'yay'
HOST = 'localhost'
PORT = 8000
DB_NAME = 'postgres'

# Flask config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'{DIALECT}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}' 

# SQLAlchemy config
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Executes text query
def make_query(query):
    result = db.session.execute(text(query))
    db.session.commit()
    return result

@app.route('/')
def homepage():
    result = make_query("""
        SELECT student_name, grade, grade_id
        FROM grades g
        JOIN students s
        ON g.student_id = s.student_id
    """)

    return render_template('home.html', results=result.all())

@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'GET':
        print('GET')
        print(request.view_args)
    elif request.method == 'POST':
        print('POST')
        id = dict(request.json)['id']
        print(f'DELETING grade_id {id}')
        make_query(f"""
            DELETE FROM grades
            WHERE grade_id = {id}
        """)
    return jsonify({'result': 'hi'})