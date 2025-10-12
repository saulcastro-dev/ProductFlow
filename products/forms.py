from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length

class ProductForm(FlaskForm):
    name = StringField('Nome do Produto:', validators=[DataRequired(), Length(max=100)], render_kw={'class': 'input', 'placeholder': 'Smartphone'})
    price = DecimalField('Preço:', validators=[DataRequired(), NumberRange(min=0)],render_kw={'class': 'input', 'placeholder': 'R$ 0,00'})
    quantity = IntegerField('Quantidade:', validators=[DataRequired(), NumberRange(min=0)], render_kw={'class': 'input', 'placeholder': '0'})
    submit = SubmitField('Enviar', render_kw={'class': 'button'})