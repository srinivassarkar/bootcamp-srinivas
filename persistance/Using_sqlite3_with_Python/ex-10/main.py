import sqlite3

class Product:
    def __init__(self):
        self.conn = sqlite3.connect('store.db')
        self.cursor = self.conn.cursor()

    def add_product(self, name, price):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a positive number")
        self.cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
        self.conn.commit()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    product = Product()
    product.add_product("Monitor", 199.99)
    product.close()