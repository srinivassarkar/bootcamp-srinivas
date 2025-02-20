import sqlite3

def transfer_funds(from_account, to_account, amount):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    try:
        cursor.execute('BEGIN TRANSACTION')
        cursor.execute('UPDATE accounts SET balance = balance - ? WHERE account_id = ?', (amount, from_account))
        cursor.execute('UPDATE accounts SET balance = balance + ? WHERE account_id = ?', (amount, to_account))
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    transfer_funds(1, 2, 100)