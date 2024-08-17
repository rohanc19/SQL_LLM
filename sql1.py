import sqlite3
import os

def setup_database():
    # Ensure the database directory exists
    os.makedirs('data', exist_ok=True)
    
    # Connect to the database
    connection = sqlite3.connect("data/student.db")
    cursor = connection.cursor()

    # Create the STUDENT table
    cursor.execute("DROP TABLE IF EXISTS STUDENT")
    cursor.execute("""
    CREATE TABLE STUDENT (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME VARCHAR(25),
        CLASS VARCHAR(25),
        SECTION VARCHAR(25),
        MARKS INT
    )
    """)

    # Insert sample data
    sample_data = [
        ('Krish', 'Data Science', 'A', 90),
        ('Sudhanshu', 'Data Science', 'A', 100),
        ('Darius', 'Data Science', 'A', 86),
        ('Vikash', 'DEVOPS', 'A', 50),
        ('Dipesh', 'DEVOPS', 'A', 35)
    ]

    cursor.executemany("""
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES (?, ?, ?, ?)
    """, sample_data)

    # Commit changes and close the connection
    connection.commit()
    connection.close()

    print("Database setup completed successfully.")

if __name__ == "__main__":
    setup_database()
    
    # Verify the data
    conn = sqlite3.connect("data/student.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM STUDENT")
    print("\nInserted records:")
    for row in cursor.fetchall():
        print(row)
    conn.close()