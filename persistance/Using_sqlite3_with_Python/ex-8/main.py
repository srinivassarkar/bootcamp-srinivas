import sqlite3

class Product:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('store.db')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def add_product(self, name, price):
        try:
            self.cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding product: {e}")

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    product = Product()
    product.add_product("Smartphone", 499.99)
    product.close()