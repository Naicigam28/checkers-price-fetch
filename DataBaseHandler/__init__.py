from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .models import Product

Base = declarative_base()
class DatabaseHandler:
    def __init__(self, db_url='sqlite:///products.db'):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_product(self, product_data):
        product = Product(**product_data)
        with self.Session() as session:
            session.add(product)
            session.commit()

    def get_all_products(self):
        with self.Session() as session:
            products = session.query(Product).all()
            return products