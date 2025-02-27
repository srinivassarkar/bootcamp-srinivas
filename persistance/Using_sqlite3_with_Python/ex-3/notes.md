# Inserting a Product into SQLite Database

### Approach

Insert a new product into the `products` table in the `store.db` SQLite database.

### Code

    import sqlite3

    def insert_product(name, price):
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
        conn.commit()
        conn.close()

    if __name__ == "__main__":
        insert_product("Laptop", 999.99)

### Run

To execute the script, run the following command in your terminal:

    python insert_product.py

<div class="note">**Note:** This content was generated using Blackbox AI.</div>