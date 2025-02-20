import sqlite3

def setup_database():
    conn = sqlite3.connect('store.db')
    conn.close()

if __name__ == "__main__":
    setup_database()