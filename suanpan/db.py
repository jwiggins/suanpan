import datetime
import os.path as op
import sqlite3

DB_FILE = op.join(op.expanduser('~'), '.suanpan.db')
INIT_SCRIPT = """CREATE TABLE transactions
    (rowid integer primary key autoincrement,
     date text,
     spender text,
     amount real,
     currency text)
"""
ADD_TRANSACTION = """
INSERT into transactions (date, spender, amount, currency) values (?, ?, ?, ?)
"""
GET_TRANSACTIONS = "SELECT * from transactions where spender = ?"


def _open_db():
    """ Open a connection to the transaction database and initialize it
    if needed.
    """
    initialize = not op.exists(DB_FILE)
    connection = sqlite3.connect(DB_FILE)

    if initialize:
        with connection:
            connection.execute(INIT_SCRIPT)

    return connection


def add_transaction(spender, amount, currency):
    """ Add a single transaction to the DB
    """
    connection = _open_db()
    date_str = datetime.datetime.utcnow().isoformat()
    with connection:
        row = (date_str, spender, amount, currency)
        connection.execute(ADD_TRANSACTION, row)


def get_all_transactions(spender):
    """ Add a single transaction to the DB
    """
    connection = _open_db()
    transactions = []
    with connection:
        for row in connection.execute(GET_TRANSACTIONS, (spender,)):
            transactions.append((row[1], row[3], row[4]))
    return transactions
