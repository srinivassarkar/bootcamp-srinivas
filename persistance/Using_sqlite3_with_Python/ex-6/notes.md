# Deleting a Product from SQLite Database

### Approach

Delete a product from the `products` table in the `store.db` SQLite database based on the product ID.

### Code

    import sqlite3

    def delete_product(product_id):
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
        conn.commit()
        conn.close()

    if __name__ == "__main__":
        delete_product(1)

### Run

To execute the script, run the following command in your terminal:

    python delete_product.py

<div class="note">**Note:** This content was generated using Blackbox AI.</div>