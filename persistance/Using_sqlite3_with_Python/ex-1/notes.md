# Setting Up SQLite Database

### Approach

Create a SQLite database named `store.db` if it doesn’t exist.

### Code

    import sqlite3

    def setup_database():
        conn = sqlite3.connect('store.db')
        conn.close()

    if __name__ == "__main__":
        setup_database()

### Run

To execute the script, run the following command in your terminal:

    python setup_db.py

<div class="note">**Note:** This content was generated using Blackbox AI.</div>
