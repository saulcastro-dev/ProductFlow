from flask import Blueprint, render_template, request, url_for, redirect
from app.extensions import db

from .models import Product
from .forms import ProductForm

product_bp = Blueprint('products', __name__, template_folder='templates')

@product_bp.route('/products')
def list_products():
    products = Product.query.all()
    
    return render_template('product_list.html', products=products)

@product_bp.route('/products/register', methods=['GET', 'POST'])
def register_product():
    form = ProductForm()
    
    if form.validate_on_submit():
        product_name = form.name.data
        product_price = form.price.data
        product_quantity = form.quantity.data
        new_product = Product(name=product_name, price=product_price, quantity=product_quantity)
        
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('products.list_products'))
    
    return render_template('register.html', form=form)

@product_bp.route('/products/update/<int:id>', methods=['GET', 'POST'])
def update_product(id):
    product = Product.query.get_or_404(id)
    form = ProductForm(obj=product)
    
    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data
        product.quantity = form.quantity.data
        
        db.session.commit()
        return redirect(url_for('products.list_products'))
    
    return render_template('update.html', form=form)

@product_bp.route('/products/delete/<int:id>', methods=['POST'])
def remove_product(id):
    product = Product.query.get_or_404(id)
    form = ProductForm(obj=product)
    db.session.delete(product)
    db.session.commit()
    
    return redirect(url_for('products.list_products'))