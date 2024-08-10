import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()

table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);

"""
cursor.execute("DROP TABLE IF EXISTS STUDENT")
cursor.execute(table_info)
cursor.execute("""Insert into STUDENT values('Krish','Data Science','A',90)""")
cursor.execute("""Insert into STUDENT values('Sudhanshu','Data Science','A',100)""")
cursor.execute("""Insert into STUDENT values('Darius','Data Science','A',86)""")
cursor.execute("""Insert into STUDENT values('Vikash','DEVOPS','A',50)""")
cursor.execute("""Insert into STUDENT values('Dipesh','DEVOPS','A',35)""")

print("The inserted records are")

data = cursor.execute("""Select * from STUDENT""")
for row in data:
    print(row)

connection.commit()
connection.close()
