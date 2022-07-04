import sqlite3 as sql

connector = sql.connect('cats.db')
cursor = connector.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS cats (
        poroda TEXT,
        age INTEGER,
        color TEXT


    )


    """
)

connector.commit()
connector.close()