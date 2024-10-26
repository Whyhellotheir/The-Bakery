from flask import Flask, request, render_template, flash, url_for, redirect, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://Jayce:Happen22%40@localhost/bakery'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(100), nullable=False)
    itemName = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

# with app.app_context():
#     db.create_all()

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

    new_order = Order(userName=userName, itemName=itemName, amount=amount)
    db.session.add(new_order)
    db.session.commit()

    return f"Thank you {userName}, for your purchase!"

if __name__ == "__main__":
    app.run(debug=True)
