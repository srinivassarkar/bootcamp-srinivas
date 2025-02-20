import sqlite3

class Product:
    def __init__(self):
        self.conn = sqlite3.connect('store.db')
        self.cursor = self.conn.cursor()

    def search_product(self, name_fragment):
        self.cursor.execute('SELECT * FROM products WHERE name LIKE ?', (f'%{name_fragment}%',))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    product = Product()
    print(product.search_product("Lap"))
    product.close()