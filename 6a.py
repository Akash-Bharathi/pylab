#Develop a CRUD program using Python-Mysql connectivity

import mysql.connector

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="myuser",
            password="mypassword",
            database="your_database"
        )
        return connection
    except mysql.connector.Error as error:
        print(" Error while connecting to MySQL:", error)
        return None

def create_record(connection, cursor):
    try:
        name = input("Enter name: ").strip()
        age = int(input("Enter age: ").strip())
        sql_query = "INSERT INTO your_table (name, age) VALUES (%s, %s)"
        cursor.execute(sql_query, (name, age))
        connection.commit()
        print(" Record created successfully.")
    except mysql.connector.Error as error:
        print(" Error while creating record:", error)

def read_records(cursor):
    try:
        sql_query = "SELECT * FROM your_table"
        cursor.execute(sql_query)
        records = cursor.fetchall()
        print("\n📋 All Records:")
        for record in records:
            print(record)
    except mysql.connector.Error as error:
        print(" Error while reading records:", error)

def update_record(connection, cursor):
    try:
        record_id = int(input("Enter ID of record to update: ").strip())
        new_name = input("Enter new name: ").strip()
        new_age = int(input("Enter new age: ").strip())
        sql_query = "UPDATE your_table SET name = %s, age = %s WHERE id = %s"
        cursor.execute(sql_query, (new_name, new_age, record_id))
        connection.commit()
        print(" Record updated successfully.")
    except mysql.connector.Error as error:
        print(" Error while updating record:", error)

def delete_record(connection, cursor):
    try:
        record_id = int(input("Enter ID of record to delete: ").strip())
        sql_query = "DELETE FROM your_table WHERE id = %s"
        cursor.execute(sql_query, (record_id,))
        connection.commit()
        print(" Record deleted successfully.")
    except mysql.connector.Error as error:
        print(" Error while deleting record:", error)

def main():
    connection = connect_to_mysql()
    if connection:
        try:
            cursor = connection.cursor()
            while True:
                print("\n CRUD Operations Menu:")
                print("1. Create Record")
                print("2. Read Records")
                print("3. Update Record")
                print("4. Delete Record")
                print("5. Exit")
                choice = input("Enter your choice (1-5): ").strip()

                if choice == '1':
                    create_record(connection, cursor)
                elif choice == '2':
                    read_records(cursor)
                elif choice == '3':
                    update_record(connection, cursor)
                elif choice == '4':
                    delete_record(connection, cursor)
                elif choice == '5':
                    break
                else:
                    print(" Invalid choice. Please enter a number between 1 and 5.")
        finally:
            cursor.close()
            connection.close()
            print(" Connection closed.")

if __name__ == "__main__":
    main()
