import unittest

from sqlalchemy import *
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import contains_eager, joinedload
from sqlalchemy.orm import relationship

#Create and engine and get the metadata
Base = declarative_base()
engine = create_engine('mssql://user:pass@Northwind', echo=True)
metadata = MetaData(bind=engine)


#Reflect each database table we need to use, using metadata
class Customer(Base):
    __table__ = Table('Customers', metadata, autoload=True)
    orders = relationship("Order", backref="customer")

class Shipper(Base):
    __table__ = Table('Shippers', metadata, autoload=True)
    orders = relationship("Order", backref="shipper")

class Employee(Base):
    __table__ = Table('Employees', metadata, autoload=True)
#    orders = relationship("Order", backref="employee")
    territories = relationship('Territory', secondary=Table('Employeeterritories', metadata, autoload=True))

class Territory(Base):
    __table__ = Table('Territories', metadata, autoload=True)
    region = relationship('Region', backref='territories')

class Region(Base):
    __table__ = Table('Region', metadata, autoload=True)


class Order(Base):
    __table__ = Table('Orders', metadata, autoload=True)
    products = relationship('Product', secondary=Table('Order Details', metadata, autoload=True))
    employee = relationship('Employee', backref='orders')

class Product(Base):
    __table__ = Table('Products', metadata, autoload=True)
    supplier = relationship('Supplier', backref='products')
    category = relationship('Category', backref='products') 

class Supplier(Base):
    __table__ = Table('Suppliers', metadata, autoload=True)

class Category(Base):
    __table__ = Table('Categories', metadata, autoload=True)


class Test(unittest.TestCase):

    def setUp(self):
        #Create a session to use the tables    
        self.session = create_session(bind=engine)        

    def tearDown(self):
        self.session.close()

    def test_withJoins(self):
        q = self.session.query(Customer)
        q = q.join(Order)
        q = q.join(Shipper)
        q = q.filter(Customer.CustomerID =='ALFKI')
        q = q.filter(Order.OrderID=='10643')
        q = q.filter(Shipper.ShipperID=='1')
        q = q.options(contains_eager(Customer.orders, Order.shipper))
        res = q.all()
        cus = res[0]
        ord = cus.orders[0]
        shi = ord.shipper
        self.assertEqual(shi.Phone, '(503) 555-9831')
