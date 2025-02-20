<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product and Category Management in SQLite</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        pre {
            background-color: #eaeaea;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            font-family: 'Courier New', Courier, monospace;
            color: #d14;
        }
        .note {
            background-color: #fff3cd;
            border-left: 6px solid #ffeeba;
            padding: 10px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <h1>Product and Category Management in SQLite</h1>
    
    <h2>Overview</h2>
    <p>This code defines a <code>Product</code> class that manages products and their associated categories in a SQLite database. It creates necessary tables and fetches products along with their categories.</p>
    
    <h2>Key Components</h2>
    <ul>
        <li><strong>Database Connection:</strong> Establishes a connection to the SQLite database and creates tables for categories and product-category relationships.</li>
        <li><strong>Table Creation:</strong> Ensures that the <code>categories</code> and <code>product_category</code> tables exist.</li>
        <li><strong>Fetching Data:</strong> Retrieves products along with their associated categories using SQL JOIN operations.</li>
    </ul>
    
    <h2>Code Breakdown</h2>
    <pre><code>import sqlite3

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

if __name__ == "__main__":
    product = Product()
    print(product.fetch_products_with_categories())
    product.close()</code></pre>
    
    <h2>Approach Simplification</h2>
    <p>The approach can be simplified into the following steps:</p>
    <ol>
        <li>Establish a connection to the SQLite database.</li>
        <li>Create tables for <code>categories</code> and the relationship between products and categories.</li>
        <li>Fetch product names along with their associated category names using SQL JOINs.</li>
        <li>Close the database connection after operations are complete.</li>
    </ol>

    <div class="note">
        <strong>Note:</strong> This content was generated using Blackbox AI.
    </div>

</body>
</html>