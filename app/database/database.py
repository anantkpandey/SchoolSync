import sqlite3

connection = sqlite3.connect(
    "schoolsync.db",
    check_same_thread=False
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth TEXT NOT NULL,
    class_name TEXT NOT NULL
)
""")

connection.commit()