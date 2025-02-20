import sqlite3

def update_price(product_id, new_price):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    update_price(1, 899.99)