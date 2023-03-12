from typing import List, Optional
from pydantic import BaseModel

class StatusBase(BaseModel):
    name: str

class StatusCreate(StatusBase):
    pass

class Status(StatusBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    orders: List[Order] = []

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    user_id: int
    status_id: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    items: List[OrderItem] = []
    status: Status
    user: User

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    products: List[Product] = []

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    title: str
    description: str
    category_id: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    category: Category

    class Config:
        orm_mode = True

class OrderItemBase(BaseModel):
    order_id: int
    product_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    id: int
    order: Order
    product: Product

    class Config:
        orm_mode = True
