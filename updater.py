import mysql.connector

mydb = mysql.connector.connect(user='ben', password='example-password',
                              host='127.0.0.1',
                              database='grocery_store_mgmt')

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM grocery_store_mgmt")

for i in mycursor:
    print(i)

# try:
#     # Establish a connection to the MySQL server
#     connection = mysql.connector.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=database
#     )

#     if connection.is_connected():
#         print("Connected to MySQL database")

#         # Create a cursor to interact with the database
#         cursor = connection.cursor()

#         # Select data from the table
#         query = f"SELECT * FROM {table_name};"
#         cursor.execute(query)

#         # Fetch all the rows
#         rows = cursor.fetchall()

#         # Print the data
#         print(f"Data from table '{table_name}':")
#         for row in rows:
#             print(row)

# except mysql.connector.Error as e:
#     print(f"Error: {e}")

# finally:
#     # Close the cursor and connection when done
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("Connection closed")
