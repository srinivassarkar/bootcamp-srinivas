import sqlite3
import csv

def export_to_csv():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    with open('products.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([i[0] for i in cursor.description])  # Write headers
        writer.writerows(cursor.fetchall())
    conn.close()

if __name__ == "__main__":
    export_to_csv()