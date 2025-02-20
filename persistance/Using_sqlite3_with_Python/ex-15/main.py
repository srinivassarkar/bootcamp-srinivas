import sqlite3

class Product:
    def __init__(self):
        self.conn = sqlite3.connect('store.db')
        self.cursor = self.conn.cursor()

    def batch_insert(self, products):
        try:
            self.conn.execute('BEGIN TRANSACTION')
            self.cursor.executemany('INSERT INTO products (name, price) VALUES (?, ?)', products)
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            print(f"Error: {e}")

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    product = Product()
    products = [("Mouse", 19.99), ("Printer", 149.99)]
    product.batch_insert(products)
    product.close()