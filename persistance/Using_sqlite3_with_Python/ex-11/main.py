import sqlite3

class Product:
    def __init__(self):
        self.conn = sqlite3.connect('store.db')
        self.cursor = self.conn.cursor()

    def add_product(self, name, price):
        try:
            self.conn.execute('BEGIN TRANSACTION')
            self.cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            print(f"Error: {e}")

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    product = Product()
    product.add_product("Keyboard", 49.99)
    product.close()