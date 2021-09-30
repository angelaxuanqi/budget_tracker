import sqlite3 as db

def init():
    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = '''
    create table if not exists expenses(
        amount number,
        category string,
        message string,
        date string)
    '''
    cur.execute(sql)
    conn.commit()


def log(amount, category, message ="", date):
    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = '''
    insert 
    '''
    cur.execute(sql)
    conn.commit()