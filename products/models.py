from app.extensions import db
from sqlalchemy import  String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

class Product(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(Numeric, nullable=False)
    quantity: Mapped[int] = mapped_column(default=0)

    def __repr__(self):
        return f'Product<{self.name}>'