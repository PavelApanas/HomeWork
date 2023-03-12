
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


from alembic.config import Config
from alembic import command


Base = declarative_base()




class Status(Base):
    __tablename__ = 'statuses'
    id = Column(Integer, primary_key=True)
    name = Column(String(10), unique=True)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(24))
    email = Column(String(24), unique=True)


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(24), unique=True)


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column(String(36))
    description = Column(String(140))
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category")


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")
    status_id = Column(Integer, ForeignKey('statuses.id'))
    status = relationship("Status")


class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship("Order")
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Product")



engine = create_engine('postgresql://user:user@localhost/mydatabase')


alembic_cfg = Config()
alembic_cfg.set_main_option("script_location", "myproject:migrations")
alembic_cfg.set_main_option("sqlalchemy.url", str(engine.url))
command.init(alembic_cfg, "myproject", directory="myproject/migrations")
command.revision(alembic_cfg, autogenerate=True)


command.upgrade(alembic_cfg, "head")



import pandas as pd
from pydantic import BaseModel

class StatusBase(BaseModel):
    name: str

class StatusCreate(StatusBase):
    pass

class UserBase(BaseModel):
    name: str
    email: str

class