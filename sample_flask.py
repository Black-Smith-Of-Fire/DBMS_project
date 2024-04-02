from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

mydb = mysql.connector.connect(
    user='ben',
    password='example-password',
    host='127.0.0.1',
    database='grocery_store_mgmt'
)

mycursor = mydb.cursor()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Redirect to the login page
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
          # Check if the provided username and password are both 'user'
        if email == 'user@gmail.com' and password == 'user':
            # If authentication successful, redirect to the customer page
            return redirect(url_for('customer'))
        else:
            # If authentication fails, render the login page again with an error message
            error_message = "Invalid username or password"
            return render_template("login.html", error=error_message)

    return render_template("login.html")

# Rest of your routes remain the same...


@app.route('/product', methods=['GET', 'POST'])
def product():
    if request.method == 'POST':
        product_id = request.form['product_id']
        product_name = request.form['product_name']
        price = request.form['price']
        quantity = request.form['quantity']
        
        # Check if product_id is not empty and is a valid integer
        if product_id and product_id.isdigit():
            product_id = int(product_id)
            # Inserting the new product
            mycursor.execute("INSERT INTO product( product_id, product_name, price, quantity ) VALUES (%s, %s, %s, %s)", ( product_id, product_name, price, quantity ))
        
        # Deleting the product if delete ID is provided and is a valid integer
        # del_id = request.form['del_id']
        # if del_id and del_id.isdigit():
        #     delete(int(del_id))
        
        mydb.commit()

    mycursor.execute("SELECT * FROM product")
    value = mycursor.fetchall()
  
    return render_template("product.html", data=value)

@app.route('/customer', methods=['GET', 'POST'])
def customer():
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        customer_name = request.form['customer_name']
        email = request.form['email']
        product = request.form['product']
        product_quantity = request.form['product_quantity']
        product_price = request.form['product_price']
        
        # Check if id is not empty and is a valid integer
        if customer_id and customer_id.isdigit():
            customer_id = int(customer_id)
            # Inserting the new product
            mycursor.execute("INSERT INTO customer( customer_id, customer_name, email, product, product_quantity, product_price ) VALUES (%s, %s, %s, %s,%s,%s)", ( customer_id, customer_name, email, product, product_quantity, product_price ))
        
        # Deleting the product if delete ID is provided and is a valid integer
        # del_id = request.form['del_id']
        # if del_id and del_id.isdigit():
            # delete(int(del_id))
        
        mydb.commit()

    mycursor.execute("SELECT * FROM customer")
    value = mycursor.fetchall()

    return render_template("customer.html", data=value,name=customer)


def delete(id):
    mycursor.execute("DELETE FROM product WHERE id = %s", (id,))
    mydb.commit()

if __name__ == "__main__":
    app.run(debug=True)
