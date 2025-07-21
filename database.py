import sqlite3
def init_db(db_name="receipts.db"): # connect to the receipts database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS receipts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vendor TEXT,
            date TEXT,
            amount TEXT,
            category TEXT
        )
    ''')
    conn.commit()
    return conn

def insert_receipt(conn, data): # Insert a parsed receipt record
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO receipts (vendor, date, amount, category)
        VALUES (?, ?, ?, ?)
    ''', (data['vendor'], data['date'], data['amount'], data['category']))
    conn.commit()

def fetch_all_receipts(conn): # Fetch all stored receipts
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM receipts')
    return cursor.fetchall()

def search_by_vendor(conn, keyword): # Search by vendor keyword
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM receipts
        WHERE LOWER(vendor) LIKE ?
    ''', ('%' + keyword.lower() + '%',))
    return cursor.fetchall()

def search_by_amount(conn, min_amt, max_amt): # Search by amount range
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM receipts
        WHERE CAST(REPLACE(REPLACE(amount, '₹', ''), ',', '') AS REAL) 
              BETWEEN ? AND ?
    ''', (min_amt, max_amt))
    return cursor.fetchall()

def sort_by_amount(conn, descending=True): # Sort receipts by amount
    cursor = conn.cursor()
    order = "DESC" if descending else "ASC"
    cursor.execute(f'''
        SELECT *, 
        CAST(REPLACE(REPLACE(amount, '₹', ''), ',', '') AS REAL) AS amt_num
        FROM receipts
        ORDER BY amt_num {order}
    ''')
    return cursor.fetchall()
