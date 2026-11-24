import sqlite3
from pathlib import Path

# set project correct path to schema file and db file

def get_connection():
    try:

        connection = sqlite3.connect('database.db')
        connection.execute("PRAGMA foreign_keys = ON")
    except Exception as exc:
        print(exc)
    return connection


# main
# control bbdd creation better unlink(missing_ok=True)

conn = get_connection()
with open('schema.sql') as f:
    conn.executescript(f.read())


'''
INSERT EXAMPLE
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )
'''

conn.close()