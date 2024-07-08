import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
    return None

def create_table(conn):
    """ create a table from the create_table_sql statement """
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS transactions (
        id integer PRIMARY KEY,
        address TEXT,
        hash TEXT,
        value INTEGER,
        time INTEGER,
        transaction_count INTEGER,
        total_received INTEGER,
        total_sent INTEGER
    );
    '''
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)

def insert_transaction(conn, transaction):
    """
    Insert a new transaction into the transactions table
    """
    sql = ''' INSERT INTO transactions(address, hash, value, time, transaction_count, total_received, total_sent)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, transaction)
    conn.commit()
    return cur.lastrowid

# Example usage
if __name__ == "__main__":
    conn = create_connection("btc_transactions.db")
    if conn is not None:
        create_table(conn)
        # Example data to insert
        transaction = ('1BoatSLRHtKNngkdXEeobR76b53LETtpyT', 'hash_here', 1000, 1598439002, 200, 500000, 400000)
        insert_transaction(conn, transaction)
        conn.close()
