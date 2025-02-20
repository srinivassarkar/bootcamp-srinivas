import sqlite3

def batch_transaction(products):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    try:
        cursor.execute('BEGIN TRANSACTION')
        cursor.executemany('INSERT INTO products (name, price) VALUES (?, ?)', products)
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    products = [("Webcam", 49.99), ("Microphone", 69.99)]
    batch_transaction(products)