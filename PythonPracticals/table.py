import mysql.connector

# Connect to MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1111",
    database="tableexp6"
)

# Create cursor
cursor = connection.cursor()

# Create Student table if not exists
cursor.execute("CREATE TABLE IF NOT EXISTS Student (sno INT AUTO_INCREMENT PRIMARY KEY, sname VARCHAR(255), result VARCHAR(255))")

# Insert records into the Student table
student_records = [
    ("John", "Pass"),
    ("Alice", "Fail"),
    ("Bob", "Pass")
]

cursor.executemany("INSERT INTO Student (sname, result) VALUES (%s, %s)", student_records)

# Commit changes
connection.commit()

# Fetch all records from the Student table
cursor.execute("SELECT * FROM Student")
records = cursor.fetchall()

# Print all records
for record in records:
    print(record)

# Close cursor and connection
cursor.close()
connection.close()
