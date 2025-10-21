import sqlite3 as sql3
import pandas as pd

connection = sql3.connect("test.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS TEST(id INTEGER PRIMARY KEY, name CHAR(25) NOT NULL, description TEXT NOT NULL)")
cursor.execute(f"""
    INSERT INTO TEST VALUES
        {", ".join([f"({index}, \"Test {index + 1}\", \"Description.\")" for index in range(1000)])}
""")
connection.commit()
cursor.close()
connection.close()