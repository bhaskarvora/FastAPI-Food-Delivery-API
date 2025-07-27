
# Imports the database connection (engine) and base class (Base) for model definitions.

from database import engine,Base

# Imports the User and Order ORM models which define the database table structures.

from models import User,Order

# Creates all tables defined by the models in the connected PostgreSQL database if they don’t already exist.
Base.metadata.create_all(bind=engine)
