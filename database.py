import sqlite3
from config import DATABASE_NAME

def create_connection():
    """SQLite bazası ilə əlaqə yaradır (fayl avtomatik yaranır)."""
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection

def setup_database():
    """Cədvəli yaradır (əgər yoxdursa)."""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Score INTEGER NOT NULL,
            Grade TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

def add_student(name, score, grade):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Students (Name, Score, Grade) VALUES (?, ?, ?)", (name, score, grade))
    connection.commit()
    connection.close()

def get_students(search_name=None):
    connection = create_connection()
    cursor = connection.cursor()
    
    if not search_name:
        cursor.execute("SELECT Name, Score, Grade FROM Students")
    else:
        cursor.execute("SELECT Name, Score, Grade FROM Students WHERE Name LIKE ?", (f"%{search_name}%",))
        
    rows = cursor.fetchall()
    students = [{"Name": row["Name"], "Score": row["Score"], "Grade": row["Grade"]} for row in rows]
    connection.close()
    return students
