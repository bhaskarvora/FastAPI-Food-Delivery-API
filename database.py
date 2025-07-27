
# Imports create_engine to establish a connection between SQLAlchemy and your PostgreSQL database.

from sqlalchemy import create_engine

# Imports declarative_base to define ORM models and sessionmaker to manage database sessions.


from sqlalchemy.orm import declarative_base,sessionmaker


#Creates a connection engine to the pizza_delivery PostgreSQL database using user postgres and password bv, and logs all SQL statements with echo=True.


engine=create_engine('postgresql://postgres:bv@localhost/pizza_delivery',
    echo=True
)

# Defines a base class Base that all your ORM models will inherit from to be mapped to database tables.

Base=declarative_base()

#  Creates a configurable Session class used to interact with the database (e.g., querying, adding, committing data).

Session=sessionmaker()