import sqlite3

class Product:
    def __init__(self):
        self.conn = sqlite3.connect('store.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS product_category (
                product_id INTEGER,
                category_id INTEGER,
                FOREIGN KEY(product_id) REFERENCES products(id),
                FOREIGN KEY(category_id) REFERENCES categories(id)
            )
        ''')
        self.conn.commit()

    def fetch_products_with_categories(self):
        self.cursor.execute('''
            SELECT products.name, categories.name 
            FROM products 
            JOIN product_category ON products.id = product_category.product_id 
            JOIN categories ON product_category.category_id = categories.id
        ''')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()