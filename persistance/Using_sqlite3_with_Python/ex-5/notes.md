# Updating Product Price in SQLite Database

### Approach

Update the price of a product in the `products` table in the `store.db` SQLite database based on the product ID.

### Code

    import sqlite3

    def update_price(product_id, new_price):
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
        conn.commit()
        conn.close()

    if __name__ == "__main__":
        update_price(1, 899.99)

### Run

To execute the script, run the following command in your terminal:

    python update_price.py

<div class="note">**Note:** This content was generated using Blackbox AI.</div>