import sqlite3

class Product:
    def __init__(self):
        self.conn = sqlite3.connect('store.db')
        self.cursor = self.conn.cursor()

    def add_product(self, name, price):
        self.cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
        self.conn.commit()

    def update_product(self, product_id, new_price):
        self.cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
        self.conn.commit()

    def list_products(self):
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    product = Product()
    product.add_product("Tablet", 299.99)
    print(product.list_products())
    product.close()