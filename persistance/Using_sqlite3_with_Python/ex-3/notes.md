<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inserting a Product into SQLite Database</title>
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

    <h1>Inserting a Product into SQLite Database</h1>

    
    <h3>Approach</h3>
    <p>Insert a new product into the <code>products</code> table in the <code>store.db</code> SQLite database.</p>
    
    <h3>Code</h3>
    <pre><code>import sqlite3

def insert_product(name, price):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_product("Laptop", 999.99)</code></pre>
    
    <h3>Run</h3>
    <p>To execute the script, run the following command in your terminal:</p>
    <pre><code>python insert_product.py</code></pre>

    <div class="note">
        <strong>Note:</strong> This content was generated using Blackbox AI.
    </div>

</body>
</html>