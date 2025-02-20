import sqlite3

def insert_product(name, price):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_product("Laptop", 999.99)