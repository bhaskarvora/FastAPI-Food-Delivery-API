from pydantic import BaseModel
from typing import Optional



# Defines a Pydantic model for signing up a new user.

class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]


    class Config:
        orm_mode=True

# Enables compatibility with ORM models like SQLAlchemy, allowing FastAPI to parse DB models directly.

        schema_extra={
            'example':{
                "username":"johndoe",
                "email":"johndoe@gmail.com",
                "password":"password",
                "is_staff":False,
                "is_active":True
            }
        }



class Settings(BaseModel):
    authjwt_secret_key:str='b4bb9013c1c03b29b9311ec0df07f3b0d8fd13edd02d5c45b2fa7b86341fa405'


# LoginModel – Schema for user login

class LoginModel(BaseModel):
    username:str
    password:str

# OrderModel – Schema for placing or reading an order

class OrderModel(BaseModel):
    id:Optional[int]
    quantity:int
    order_status:Optional[str]="PENDING"
    pizza_size:Optional[str]="SMALL"
    user_id:Optional[int]


    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "quantity":2,
                "pizza_size":"LARGE"
            }
        }


# OrderStatusModel – Schema for updating order status

class OrderStatusModel(BaseModel):
    order_status:Optional[str]="PENDING"

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "order_status":"PENDING"
            }
        }