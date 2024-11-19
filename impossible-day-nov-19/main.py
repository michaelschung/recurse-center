import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port=8000,
    dbname='postgres',
    user='postgres',
    password='password',
)

cur = conn.cursor()

cur.execute('''
    DROP TABLE IF EXISTS test_table
''')

cur.execute('''
            CREATE TABLE IF NOT EXISTS test_table (
                id SERIAL PRIMARY KEY,
                key INT,
                val VARCHAR(255)
            )
''')

cur.execute('''
            INSERT INTO test_table (key, val) VALUES
                (10, 'Hello'),
                (20, 'Goodbye')
''')

cur.execute('''
            SELECT *
            FROM test_table
            WHERE key < 30
''')

print(cur.fetchall())

conn.commit()

cur.close()
conn.close()