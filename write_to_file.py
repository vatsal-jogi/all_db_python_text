# Import necessary libraries
import mysql.connector
from pymongo import MongoClient
import sqlite3

# Function to write data to a text file
def write_data_to_file(filename):
    with open(filename, 'w') as file:
        # MySQL data retrieval
        try:
            import mysql.connector
        except ImportError:
            print("MySQL connector is not installed. Please install it using 'pip install mysql-connector-python'.")
            return  # Exit the function if the module is not available

        try:
            mydb = mysql.connector.connect(host='localhost', user='root', password='', database='users')
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM users")
            mysql_data = mycursor.fetchall()
            file.write("MySQL Data:\n")
            for row in mysql_data:
                file.write(f"{row}\n")
        except mysql.connector.Error as error:
            print('Failed to read from MySQL:', error)

        # MongoDB data retrieval
        try:
            client = MongoClient('mongodb+srv://vtsljogi009:vatsal123@cluster0.mimsx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
            db = client['user']
            collection = db['users']
            mongo_data = collection.find()
            file.write("\nMongoDB Data:\n")
            for document in mongo_data:
                file.write(f"{document}\n")
            client.close()
        except Exception as error:
            print('Failed to read from MongoDB:', error)

        # SQLite data retrieval
        try:
            cnt = sqlite3.connect('sqlite.db')
            cursor = cnt.cursor()
            cursor.execute("SELECT * FROM users")
            sqlite_data = cursor.fetchall()
            file.write("\nSQLite Data:\n")
            for row in sqlite_data:
                file.write(f"{row}\n")
            cnt.close()
        except sqlite3.Error as error:
            print('Failed to read from SQLite:', error)

# Call the function to write data to 'output.txt'
write_data_to_file('output.txt') 