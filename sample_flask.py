from flask import Flask, render_template , url_for, request, redirect

import mysql.connector


mydb = mysql.connector.connect(user='ben', password='example-password',
                              host='127.0.0.1',
                              database='grocery_store_mgmt')

mycursor = mydb.cursor()

app = Flask(__name__)  

@app.route('/index')
def customer():
  mycursor.execute("SELECT * FROM customer")
  value = mycursor.fetchall()
  return render_template("index.html",data=value,name=customer)

@app.route('/products')
def product():
  mycursor.execute("SELECT * FROM product")
  value2 = mycursor.fetchall()
  return render_template("index.html",data=value2,name=product)

@app.route('/administrator')
def admin():
  mycursor.execute("SELECT * FROM administrator")
  value3 = mycursor.fetchall()
  return render_template("index.html",data=value3,name=administrator)
  
@app.route('/cart')
def cart():
  mycursor.execute("SELECT * FROM cart")
  value4 = mycursor.fetchall()
  return render_template("index.html",data=value4,name=cart)

@app.route('/invoice')
def invoice():
  mycursor.execute("SELECT * FROM invoice")
  value5 = mycursor.fetchall()
  return render_template("index.html",data=value5,name=invoice)

if __name__ == "__main__":
  app.run(debug=True) 