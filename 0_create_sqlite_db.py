# %%
import sqlite3
from sqlalchemy import create_engine

# %%
# Create df (if doesn't exist)
def create_sqlite_database(filename):
    conn = None

    try:
        conn = sqlite3.connect(filename) # if db does not exist, to connect sqlite creates the db
        print(sqlite3.sqlite_version)

    except sqlite3.Error as error:
        print(error)

    finally:
        if conn:
            conn.close()

# %%
if __name__ == '__main__':
    create_sqlite_database("DAP_database.db")

# Create engine to establish connection 
engine = create_engine("sqlite:///DAP_database.db")

# %%



