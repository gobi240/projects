import mysql.connector

# Connect to MySQL Server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)

cursor = conn.cursor()

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS studentdb")

# Select Database
cursor.execute("USE studentdb")

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    department VARCHAR(50)
)
""")

# Get Data from User
print("Enter Student Details")

sid = int(input("Enter ID: "))
name = input("Enter Name: ")
age = int(input("Enter Age: "))
dept = input("Enter Department: ")

# Insert Data
sql = "INSERT INTO students (id, name, age, department) VALUES (%s, %s, %s, %s)"
values = (sid, name, age, dept)

cursor.execute(sql, values)
conn.commit()

print("\nData Inserted Successfully!")

# Display Data
print("\nStudent Records")
print("-" * 50)

cursor.execute("SELECT * FROM students")

records = cursor.fetchall()

for row in records:
    print("ID:", row[0])
    print("Name:", row[1])
    print("Age:", row[2])
    print("Department:", row[3])
    print("-" * 50)

# Close Connection
cursor.close()
conn.close()
