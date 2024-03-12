import mysql.connector

mydb = mysql.connector.connect(user='ben', password='example-password',
                              host='127.0.0.1',
                              database='grocery_store_mgmt')

mycursor = mydb.cursor()

print("Enter the table to edit")
table=input()
print("\n")

print("Enter the id ")
id = input()
print("\n")

print("Enter the name")
name = input()
print("\n")

print("Enter the location")
location = input()
print("\n")

print("Enter the email")
email = input()
print("\n")

print("Enter the mod date")
mod_date = input()
print("\n")

print("Enter the c_date")
c_date = input()
print("\n")


# Use placeholders to prevent SQL injection
sql = "INSERT INTO {table} VALUES (%s, %s, %s, %s, %s, %s)"
values = (id, location, name, email, c_date, mod_date)

mycursor.execute(sql, values)

mydb.commit()  # Commit the changes to the database

print(mycursor.rowcount, "record inserted.")
