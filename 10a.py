#10(A) Develop an e-commerce store application with features like product listings , user authentication , shopping cart management and secure payment integration

# Example of simplified code using Flask framework and SQLite database
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Routes
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

# Placeholder for future routes:
# - @app.route('/register')
# - @app.route('/login')
# - @app.route('/add_to_cart/<int:product_id>')
# - @app.route('/cart')
# - @app.route('/checkout')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
