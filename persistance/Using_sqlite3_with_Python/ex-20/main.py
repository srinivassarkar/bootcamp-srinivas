import sqlite3

def update_inventory(product_id, quantity_change):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    try:
        cursor.execute('BEGIN TRANSACTION')
        cursor.execute('UPDATE products SET stock = stock + ? WHERE id = ?', (quantity_change, product_id))
        cursor.execute('INSERT INTO inventory_log (product_id, change) VALUES (?, ?)', (product_id, quantity_change))
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    update_inventory(1, -5)