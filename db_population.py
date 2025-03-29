import sqlite3

# TODO: use sqlalchemy to create a more complex db.
# TODO: change to postgress in the cloud.

with sqlite3.connect('tenders.sqlite') as conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE TENDERS (id VARCHAR, title VARCHAR)')
    conn.commit()
