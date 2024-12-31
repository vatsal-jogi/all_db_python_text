# import mysql.connector
# try:
#     mydb=mysql.connector.connect(host='localhost',user='root',password='')
#     mycursor=mydb.cursor()
#     mycursor.execute("create database users")
#     print('database is created successfully')
# except mysql.connector.Error as error:
#     print('Failed to create database', error)   



# import mysql.connector
# try:    
#     mydb=mysql.connector.connect(host='localhost',user='root',password='',database='users')
#     mycursor=mydb.cursor()
#     mycursor.execute("create table users (id integer primary key auto_increment, name text(20),email text(50) , password text(50))")
#     print('table is created successfully')
# except mysql.connector.Error as error:
#     print('Failed to create table', error)   

import mysql.connector

# Establish the database connection
try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='users'  # Ensure the 'users' database exists
    )

    mycursor = mydb.cursor()

    # Insert data for 10 people (without including the `id` field)
    data = [
        ('John Doe', 'johndoe@example.com', 'password123'),
        ('Alice Smith', 'alice.smith@example.com', 'alicepassword'),
        ('Bob Brown', 'bob.brown@example.com', 'bobpassword'),
        ('Charlie Davis', 'charlie.davis@example.com', 'charliepassword'),
        ('David Wilson', 'david.wilson@example.com', 'davidpassword'),
        ('Eva Johnson', 'eva.johnson@example.com', 'evapassword'),
        ('Frank Clark', 'frank.clark@example.com', 'frankpassword'),
        ('Grace Lewis', 'grace.lewis@example.com', 'gracepassword'),
        ('Henry Walker', 'henry.walker@example.com', 'henrypassword'),
        ('Ivy Martin', 'ivy.martin@example.com', 'ivypassword')
    ]

    # Insert data using the execute many method (omitting the `id` column)
    insert_query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    mycursor.executemany(insert_query, data)

    # Commit the transaction
    mydb.commit()

    print('10 records have been inserted successfully into the table.')

except mysql.connector.Error as error:
    print('Failed to insert data:', error)
finally:
    # Close the cursor and the connection
    if mycursor:
        mycursor.close()
    if mydb:
        mydb.close()
