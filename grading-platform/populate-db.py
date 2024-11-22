from sqlalchemy import create_engine, text

default = True

DIALECT = 'postgresql+psycopg2'
USERNAME = 'postgres' if default else 'michaelchung'
PASSWORD = 'password' if default else 'yay'
HOST = 'localhost'
PORT = 8000
DB_NAME = 'postgres'

def my_query(conn, query):
    return conn.execute(text(query))

def main():
    conn_str = f'{DIALECT}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
    print(f'Connecting to {conn_str}...')

    engine = create_engine(conn_str)

    with engine.connect() as conn:
        result = my_query(conn, """DROP TABLE IF EXISTS grades, students""")

        result = my_query(conn, """
            CREATE TABLE IF NOT EXISTS students (
                student_id SERIAL PRIMARY KEY,
                student_name VARCHAR(255)
            )
        """)

        result = my_query(conn, """
            CREATE TABLE IF NOT EXISTS grades (
                grade_id SERIAL PRIMARY KEY,
                student_id INT REFERENCES students,
                grade INT
            )
        """)

        result = my_query(conn, """
            INSERT INTO students (student_name) VALUES
                ('Emily'),
                ('Michael'),
                ('Walter')
        """)

        result = my_query(conn, """
            INSERT INTO grades (student_id, grade) VALUES
                (1, 98),
                (3, 104),
                (2, 83)
        """)

        result = my_query(conn, """
            SELECT student_name, grade
            FROM grades g
            JOIN students s
            ON g.student_id = s.student_id
        """)

        print(result.all())

        conn.commit()

if __name__ == '__main__':
    main()