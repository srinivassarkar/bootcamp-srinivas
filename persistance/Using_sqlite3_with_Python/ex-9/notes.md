<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Class with Search Functionality for SQLite Database</title>
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

    <h1>Product Class with Search Functionality for SQLite Database</h1>
    

    
    <h3>Approach</h3>
    <p>Create a <code>Product</code> class to manage products in the <code>products</code> table of the <code>store.db</code> SQLite database. This class includes a method to search for products by a name fragment.</p>
    
    <h3>Code</h3>
    <pre><code>import sqlite3

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
    product.close()</code></pre>
    
    <h3>Run</h3>
    <p>To execute the script, run the following command in your terminal:</p>
    <pre><code>python product.py</code></pre>

    <div class="note">
        <strong>Note:</strong> This content was generated using Blackbox AI.
    </div>

</body>
</html>