from flask import Flask, request, render_template, url_for, redirect
from wishlist.models import Item, db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app


app = create_app()


@app.get('/')
def home():
    wishlist = Item.query.all()
    return render_template('wishlist/index.html', wishlist=wishlist, title=' Главная страница')


@app.post('/add')
def add():
    title = request.form.get('title')
    description = request.form.get('description')
    price = request.form.get('price')
    new_item = Item(title=title, description=description, price=price, is_complete=False)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('home'))


@app.get('/update/<int:item_id>')
def update(item_id):
    item = Item.query.filter_by(id=item_id).first()
    item.is_complete = not item.is_complete
    db.session.commit()
    return redirect(url_for('home'))


@app.get('/delete/<int:item_id>')
def delete(item_id):
    item = Item.query.filter_by(id=item_id).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('home'))

