import sqlite3

def basic_transaction():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    try:
        cursor.execute('BEGIN TRANSACTION')
        cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', ("Headphones", 59.99))
        cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', ("Speaker", 79.99))
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    basic_transaction()