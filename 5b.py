#5(b) Develop a Python program to insert records into a table in MySQL using user input and display a confirmation message upon successful insertion.

import mysql.connector

# Connect to MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="myuser",
        password="mypassword",
        database="your_database"
    )
    cursor = conn.cursor()

    # Get user input
    name = input("Enter name: ").strip()
    age_input = input("Enter age: ").strip()

    # Basic input validation
    if not age_input.isdigit():
        print("Invalid age. Please enter a number.")
    else:
        age = int(age_input)

        # Insert record using parameterized query
        sql = "INSERT INTO your_table (name, age) VALUES (%s, %s)"
        cursor.execute(sql, (name, age))
        conn.commit()
        print(" Record inserted successfully.")

except mysql.connector.Error as err:
    print(" Database error:", err)

finally:
    # Always close resources
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
