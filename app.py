from flask import Flask, request, render_template, flash, url_for, redirect, get_flashed_messages
import json

app = Flask(__name__)

#renders the html form
@app.route('/')

def home():
    return render_template('baking.html')

@app.route('/placeOrder')
def place_order():
    return render_template('placeOrder.html')

@app.route('/aboutMe')
def about_me():
    return render_template('aboutMe.html')


# handle form submission and turning inputs to json
@app.route("/submit", methods=["POST"])
def submit():
    amount = request.form.get("amount")
    userName = request.form.get("userName")
    itemName = request.form.get("itemName")

    order_name = {
        "userName": userName,
        "itemName": itemName,
        "amount": amount
    }

        # Load existing orders
    try:
        with open('orders.json', 'r') as f:
            orders = json.load(f)
    except FileNotFoundError:
        orders = []  # If file doesn't exist, start with an empty list

    # Append the new order
    orders.append(order_name)

    # Save all orders back to the JSON file
    with open('orders.json', 'w') as f:
        json.dump(orders, f, indent=4)  # Pretty-print the JSON

    return f"Thank you {userName}, for your purchase!"

if __name__ == "__main__":
    app.run(debug=True)
