
# Imports the Base class from database.py to define SQLAlchemy models (tables).
from database import Base

# Imports essential column types and constraints used for defining table schema.
from sqlalchemy import Column,Integer,Boolean,Text,String,ForeignKey

# Imports relationship to define the connection between two tables (like foreign key relationships).

from sqlalchemy.orm import relationship

# Imports ChoiceType to restrict column values to a predefined set of choices.

from sqlalchemy_utils.types import ChoiceType


# Defines a model User that inherits from SQLAlchemy's Base class, mapping it to a table.

# User Table:
# Stores user information like username, email, hashed password, account status (is_active), and admin role (is_staff).

# Has a one-to-many relationship with Order, meaning each user can place multiple orders.



class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    username=Column(String(25),unique=True)
    email=Column(String(80),unique=True)
    password=Column(Text,nullable=True)
    is_staff=Column(Boolean,default=False)
    is_active=Column(Boolean,default=False)
    orders=relationship('Order',back_populates='user')


    def __repr__(self):
        return f"<User {self.username}"



# Order Table:
# Stores order details including quantity, pizza size, order status, and the user who placed it (user_id).

# Uses ChoiceType to enforce valid values for order_status (e.g., "PENDING") and pizza_size (e.g., "SMALL").

class Order(Base):

    ORDER_STATUSES=(
        ('PENDING','pending'),
        ('IN-TRANSIT','in-transit'),
        ('DELIVERED','delivered')

    )

    PIZZA_SIZES=(
        ('SMALL','small'),
        ('MEDIUM','medium'),
        ('LARGE','large'),
        ('EXTRA-LARGE','extra-large')
    )


    __tablename__='orders'
    id=Column(Integer,primary_key=True)
    quantity=Column(Integer,nullable=False)
    order_status=Column(ChoiceType(choices=ORDER_STATUSES),default="PENDING")
    pizza_size=Column(ChoiceType(choices=PIZZA_SIZES),default="SMALL")
    user_id=Column(Integer,ForeignKey('user.id'))
    user=relationship('User',back_populates='orders')

    def __repr__(self):
        return f"<Order {self.id}>"