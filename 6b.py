#6(b) Develop a Python program to manage student records in a MySQL database, allowing users to add, view, update, and delete student information.

import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="myuser",
    passsword="mypassword",
    database="your_database"
)
cursor = conn.cursor()

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            course VARCHAR(100)
        )
    ''')
    conn.commit()

def add_student():
    name = input("Enter name: ").strip()
    age = int(input("Enter age: ").strip())
    course = input("Enter course: ").strip()
    cursor.execute("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)", (name, age, course))
    conn.commit()
    print(" Student added successfully.")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n Student Records:")
    for row in rows:
        print(row)

def update_student():
    student_id = int(input("Enter student ID to update: ").strip())
    name = input("New name: ").strip()
    age = int(input("New age: ").strip())
    course = input("New course: ").strip()
    cursor.execute("UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s", (name, age, course, student_id))
    conn.commit()
    print(" Record updated successfully.")

def delete_student():
    student_id = int(input("Enter student ID to delete: ").strip())
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    print(" Record deleted successfully.")

# Create table if it doesn't exist
create_table()

# Menu loop
while True:
    print("\n Student Management System:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print(" Invalid choice. Please enter a number between 1 and 5.")

# Close DB connection
cursor.close()
conn.close()
print(" Connection closed.")
