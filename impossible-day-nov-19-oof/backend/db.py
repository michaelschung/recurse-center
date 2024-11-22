import psycopg2

def setup_database():
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_db_user",
        password="your_db_password",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # Create the table if not exists and insert a single row
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            val TEXT NOT NULL
        );
    """)
    cursor.execute("INSERT INTO test_table (val) VALUES ('hello') ON CONFLICT DO NOTHING;")
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    setup_database()
