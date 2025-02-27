# Fetching Products from SQLite Database

### Approach

Fetch all products from the `products` table in the `store.db` SQLite database and print them.

### Code

    import sqlite3

    def fetch_products():
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products')
        products = cursor.fetchall()
        for product in products:
            print(product)
        conn.close()

    if __name__ == "__main__":
        fetch_products()

### Run

To execute the script, run the following command in your terminal:

    python fetch_products.py

<div class="note">**Note:** This content was generated using Blackbox AI.</div>