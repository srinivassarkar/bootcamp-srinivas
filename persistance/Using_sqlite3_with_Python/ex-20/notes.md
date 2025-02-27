<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inventory Update Management in SQLite</title>
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

    <h1>Inventory Update Management in SQLite</h1>
    
    <h2>Overview</h2>
    <p>This code defines a function <code>update_inventory</code> that demonstrates how to update the inventory of a product in a SQLite database while logging the changes.</p>
    
    <h2>Key Components</h2>
    <ul>
        <li><strong>Database Connection:</strong> Establishes a connection to the SQLite database.</li>
        <li><strong>Transaction Management:</strong> Uses a transaction to ensure that both the stock update and the log entry are treated as a single unit of work.</li>
        <li><strong>Stock Update:</strong> Updates the stock of the specified product by applying the quantity change.</li>
        <li><strong>Inventory Logging:</strong> Inserts a record into the <code>inventory_log</code> table to track the change in inventory.</li>
        <li><strong>Error Handling:</strong> Catches errors and rolls back the transaction if any issues occur during the update.</li>
        <li><strong>Closing Connection:</strong> Ensures the database connection is closed after operations are complete.</li>
    </ul>
    
    <h2>Code Breakdown</h2>
    <pre><code>import sqlite3

def update_inventory(product_id, quantity_change):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    try:
        cursor.execute('BEGIN TRANSACTION')
        cursor.execute('UPDATE products SET stock = stock + ? WHERE id = ?', (quantity_change, product_id))
        cursor.execute('INSERT INTO inventory_log (product_id, change) VALUES (?, ?)', (product_id, quantity_change))
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    update_inventory(1, -5)</code></pre>
    
    <h2>Approach Simplification</h2>
    <p>The approach can be simplified into the following steps:</p>
    <ol>
        <li>Establish a connection to the SQLite database.</li>
        <li>Begin a transaction to ensure that both operations are treated as a single unit.</li>
        <li>Update the stock of the specified product by applying the quantity change.</li>
        <li>Log the inventory change in the <code>inventory_log</code> table.</li>
        <li>Commit the transaction if both operations succeed; otherwise, roll back in case of an error.</li>
        <li>Close the database connection after operations are complete.</li>
    </ol>

    <div class="note">
        <strong>Note:</strong> This content was generated using Blackbox AI.
    </div>

</body>
</html>