from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auction.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)

@app.route('/')
def index():
    items = Item.query.all()
    return render_template('home.html', items=items)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']

        item = Item(name=name, price=price)
        db.session.add(item)
        db.session.commit()

        return redirect('/')

    return render_template('create.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
