import sqlite3
from pathlib import Path

# set schema file and db file
DB_FOLDER_PATH = Path(__file__).resolve().parent 
PROJECT_PATH = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_PATH / "data"
DATABASE_PATH = DATA_PATH / "database.db"



def connect_to_database(db_path):
    try:

        # connect and create database
        connection = sqlite3.connect(db_path)
        # activate foreign keys
        connection.execute("PRAGMA foreign_keys = ON")
    except Exception as exc:
        print(exc)
    return connection

# main
if __name__ == "__main__":

    try:

        # data folder if not exist
        DATA_PATH.mkdir(parents=True, exist_ok=True)

        # remove bbdd if exist
        DATABASE_PATH.unlink(missing_ok=True)    
        
        # create bbdd with foreign keys ativate
        conn = connect_to_database(DATABASE_PATH) 
        # add tables based on schema.sql
        with open(DB_FOLDER_PATH /"schema.sql") as f:
            conn.executescript(f.read())
            print("database created")


    except Exception as exc:
        print(exc)
    finally:
        # close bbdd connection
        conn.close()
