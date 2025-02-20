import sqlite3

class Product:
    def __init__(self):
        self.conn = sqlite3.connect('store.db')
        self.cursor = self.conn.cursor()

    def total_value(self):
        self.cursor.execute('SELECT SUM(price) FROM products')
        return self.cursor.fetchone()[0]

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    product = Product()
    print(f"Total value: {product.total_value()}")
    product.close()