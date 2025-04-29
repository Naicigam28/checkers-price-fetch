from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    desc = Column(String)
    barcode = Column(String)
    brand = Column(String)
    price = Column(Float)
    url = Column(String)  # New field for product URL

    def __init__(self, name, desc, barcode, brand, price, url):
        self.name = name
        self.desc = desc
        self.barcode = barcode
        self.brand = brand
        self.price = price
        self.url = url
