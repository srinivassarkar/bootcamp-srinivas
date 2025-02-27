# Creating a Table in SQLite Database

### Approach

Create a table named `products` in the `store.db` SQLite database if it doesn’t already exist.

### Code

    import sqlite3

    def create_table():
        conn = sqlite3.connect('store.db')
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

### Run

To execute the script, run the following command in your terminal:

    python create_table.py

<div class="note">**Note:** This content was generated using Blackbox AI.</div>