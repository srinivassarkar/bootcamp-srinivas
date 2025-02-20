import sqlite3

def fetch_products():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(product)
    conn.close()

if __name__ == "__main__":
    fetch_products()