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

@app.route('/deleteGrade', methods=['GET', 'POST'])
def deleteGrade():
    if request.method == 'POST':
        id = dict(request.json)['id']
        make_query(f"""
            DELETE FROM grades
            WHERE grade_id = {id}
        """)
        return jsonify({'result': 'DELETED'})
    return jsonify({'result': '?'})

@app.route('/addGrade', methods=['POST'])
def addGrade():
    if request.method == 'POST':
        new_grade = request.form
        name = new_grade.get('inputName')
        grade = new_grade.get('inputGrade')
        make_query(f"""
            WITH new_student AS (
                INSERT INTO students (student_name)
                SELECT '{name}'
                WHERE NOT EXISTS (
                    SELECT 1 FROM students WHERE student_name = '{name}'
                )
                RETURNING student_id
            )
            INSERT INTO grades (student_id, grade)
            SELECT
                COALESCE((SELECT student_id FROM new_student), student_id),
                {grade}
            FROM students
            WHERE student_name = '{name}'
        """)
        return jsonify({'result': 'ADDED'})
    return jsonify({'result': '?'})