import sqlite3
from contextlib import contextmanager
database = './database.db'

# Create a connection to the database
@contextmanager
def create_connection(database):
    connection = sqlite3.connect(database)
    connection.execute("PRAGMA foreign_keys = ON")
    try:
        yield connection
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()

# A function that creates a table
def create_table(connection, sql_command):
    """ Create a table from sql_command statement"""
    try:
        c = connection.cursor()
        c.execute(sql_command)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':

    sgl_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname VARCHAR(100),
        email VARCHAR(300) UNIQUE
    );
    """

    sgl_create_status_table = """
    CREATE TABLE IF NOT EXISTS status (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) UNIQUE
    );
    """

    sql_values_to_status = """
    INSERT INTO status (name) VALUES ('new'),('in progress'), ('completed');
    """

    sgl_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100),
    description TEXT,
    status_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (status_id) REFERENCES status (id),
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE ON UPDATE CASCADE
    )
    """

    with create_connection(database) as conn:
        if conn is not None: 
            create_table(conn,sgl_create_users_table)
            create_table(conn,sgl_create_status_table)
            create_table(conn,sql_values_to_status)
            create_table(conn,sgl_create_tasks_table)
        else:
            print('Error! Cannot create the database connection!')


    




