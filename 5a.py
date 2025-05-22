#5(a) Develop a Python program to fetch records from a table in MySQL and display the results.

import mysql.connector

def fetch_records_from_mysql():
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="your_database"
        )

        # Create cursor object
        cursor = connection.cursor()

        # Write SQL query to fetch records from table
        sql_query = "SELECT * FROM your_table"

        # Execute SQL query
        cursor.execute(sql_query)

        # Fetch all records
        records = cursor.fetchall()

        # Display fetched records
        for record in records:
            print(record)

    except mysql.connector.Error as error:
        print("Error while fetching records from MySQL:", error)

    finally:
        # Close cursor and connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Call the function to fetch and display records
fetch_records_from_mysql()
