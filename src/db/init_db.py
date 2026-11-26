import sqlite3
from pathlib import Path

# set schema file and db file paths
DB_FOLDER_PATH = Path(__file__).resolve().parent 
PROJECT_PATH = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_PATH / "data"
DATABASE_PATH = DATA_PATH / "database.db"

def connect_to_database(db_path):    

    # connect and create database
    connection = sqlite3.connect(db_path)
    # activate foreign keys
    connection.execute("PRAGMA foreign_keys = ON")
   
    return connection

# main
if __name__ == "__main__":

    conn = None
    try:

        # create data folder if not exist
        DATA_PATH.mkdir(parents=True, exist_ok=True)

        # read schema first: fail before touching the DB
        with open(DB_FOLDER_PATH /"schema.sql", encoding="utf-8") as f:
            # get schema
            schema_sql = f.read()

        # remove bbdd if exist
        DATABASE_PATH.unlink(missing_ok=True)    
            
        # create bbdd with foreign keys ativate
        conn = connect_to_database(DATABASE_PATH) 
        conn.executescript(schema_sql)
        print("database created")

    except Exception as exc:
        print(exc) 
        # if connection is open, close and remove ddbb
        if conn is not None:
            conn.close()
            conn = None
            DATABASE_PATH.unlink(missing_ok=True)
        raise
    finally:
        if conn is not None:
            conn.close()

            
            
