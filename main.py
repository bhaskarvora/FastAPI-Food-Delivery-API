# Import FastAPI to create the web app instance

from fastapi import FastAPI


# Import the authentication and order routes 
from auth_routes import auth_router
from order_routes import order_router

# Import AuthJWT class to handle JWT-based authentication

from fastapi_jwt_auth import AuthJWT

# Import Settings class which defines the secret key for JWT
from schemas import Settings
import inspect, re
from fastapi import FastAPI

# For customizing the OpenAPI schema (used by Swagger UI)
from fastapi.routing import APIRoute
from fastapi.openapi.utils import get_openapi

app=FastAPI()

# Customizes the Swagger UI to include JWT Bearer Auth


def custom_openapi():

    # If schema is already used then reuse it 
    if app.openapi_schema:
        return app.openapi_schema
    
    # Generate base OpenAPI schema with title, version, description, and routes

    openapi_schema = get_openapi(
        title = "Pizza Delivery API",
        version = "1.0",
        description = "An API for a Pizza Delivery Service",
        routes = app.routes,
    )

    # Define Bearer token authentication scheme

    openapi_schema["components"]["securitySchemes"] = {
        "Bearer Auth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Enter: **'Bearer &lt;JWT&gt;'**, where JWT is the access token"
        }
    }

     # Filter only API routes (skip static/internal routes)
    api_router = [route for route in app.routes if isinstance(route, APIRoute)]

    for route in api_router:
        path = getattr(route, "path")
        endpoint = getattr(route,"endpoint")
        methods = [method.lower() for method in getattr(route, "methods")]

        for method in methods:
            # access_token
            if (
                re.search("jwt_required", inspect.getsource(endpoint)) or
                re.search("fresh_jwt_required", inspect.getsource(endpoint)) or
                re.search("jwt_optional", inspect.getsource(endpoint))
            ):
                

                # If JWT protection found, add security info to Swagger path
                openapi_schema["paths"][path][method]["security"] = [
                    {
                        "Bearer Auth": []
                    }
                ]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@AuthJWT.load_config
def get_config():
    return Settings()



# Register the authentication routes (login, signup, refresh token, etc.)

app.include_router(auth_router)


# Register the order-related routes (create order, get order, delete order, etc.)

app.include_router(order_router)




#Working of this file 

# First Create the FastAPI Instance
# Load JWT Configuration
# Customizes OpenAPI / Swagger UI to support JWT auth header
# Also we have implemented the security configuration
# Include route files (auth_routes.py / order_routes.py ) to modularize the API 

# Summary
# Component	Role
# FastAPI():	App instantiation
# AuthJWT : 	Manages token-based auth
# custom_openapi() : 	Enables JWT support in Swagger
# include_router() :	Integrates routes for user and order management
# Settings() :	Securely configures JWT secret