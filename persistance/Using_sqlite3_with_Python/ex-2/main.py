import sqlite3

def create_table():
    conn = sqlite3.connect('store.db')
    # `cursor = conn.cursor()` is creating a cursor object that allows you to interact with the
    # database by executing SQL queries and fetching results. The cursor object is used to execute SQL
    # commands and navigate through the result set returned by the database queries.
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()