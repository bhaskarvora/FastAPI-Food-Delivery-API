## PIZZA DELIVERY API
A RESTful API designed for a pizza delivery service, built using FastAPI, SQLAlchemy, and PostgreSQL—created for educational purposes and hands-on learning.


## ROUTES TO IMPLEMENT
POST Routes
/auth/signup/
➤ Register a new user
➤ Access: All users

/auth/login/
➤ Login an existing user
➤ Access: All users

/orders/order/
➤ Place a new pizza order
➤ Access: All users

PUT Routes
/orders/order/update/{order_id}/
➤ Update an existing order’s details (e.g., quantity, size)
➤ Access: All users

/orders/order/status/{order_id}/
➤ Update the status of an order (e.g., Pending → Delivered)
➤ Access: Superuser only

DELETE Route
/orders/order/delete/{order_id}/
➤ Delete or cancel an existing order
➤ Access: All users

GET Routes
/orders/user/orders/
➤ Retrieve all orders made by the currently logged-in user
➤ Access: All users

/orders/orders/
➤ Retrieve all orders from all users (admin view)
➤ Access: Superuser only

/orders/orders/{order_id}/
➤ Retrieve a specific order by ID (admin view)
➤ Access: Superuser only

/orders/user/order/{order_id}/
➤ Retrieve a specific order placed by the currently logged-in user
➤ Access: All users

/docs/
➤ View the API documentation via Swagger UI
➤ Access: All users



## How to run the Project
- Install Postgreql
- Install Python
- Git clone the project with ``` git clone https://github.com/your_username/Pizza-Delivery-API.git```
- Create your virtualenv with `Pipenv` or `virtualenv` and activate it.
- Install the requirements with ``` pip install -r requirements.txt ```
- Set Up your PostgreSQL database and set its URI in your ```database.py```
```
engine=create_engine('postgresql://postgres:<username>:<password>@localhost/<db_name>',
    echo=True
)
```

- Create your database by running ``` python init_db.py ```
- Finally run the API
``` uvicorn main:app ``
