from flask import render_template, url_for, redirect
from app import app
from app.models import db, Product
from app.forms import ProductForm

@app.route('/')
def list_products():
    products = Product.query.all()
    
    return render_template('index.html', products=products)

@app.route('/products/register', methods=['GET', 'POST'])
def register_product():
    form = ProductForm()
    
    if form.validate_on_submit():
        product_name = form.name.data
        product_price = form.price.data
        product_quantity = form.quantity.data
        new_product = Product(name=product_name, price=product_price, quantity=product_quantity)
        
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('list_products'))
    
    return render_template('register.html', form=form)

@app.route('/products/update/<int:id>', methods=['GET', 'POST'])
def update_product(id):
    product = Product.query.get_or_404(id)
    form = ProductForm(obj=product)
    
    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data
        product.quantity = form.quantity.data
        
        db.session.commit()
        return redirect(url_for('list_products'))
    
    return render_template('update.html', form=form)

@app.route('/products/<int:id>', methods=['POST'])
def remove_product(id):
    product = Product.query.get_or_404(id)
    form = ProductForm(obj=product)
    db.session.delete(product)
    db.session.commit()
    
    return redirect(url_for('list_products'))