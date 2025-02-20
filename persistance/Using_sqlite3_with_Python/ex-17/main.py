import sqlite3

def multi_table_transaction():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    try:
        cursor.execute('BEGIN TRANSACTION')
        cursor.execute('INSERT INTO orders (order_date) VALUES (date("now"))')
        order_id = cursor.lastrowid
        cursor.execute('INSERT INTO order_details (order_id, product_id, quantity) VALUES (?, ?, ?)', (order_id, 1, 2))
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    multi_table_transaction()