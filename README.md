
E-Commerce Backend API - README


This project is a backend application for an e-commerce platform built using Python and Django REST Framework. It provides APIs for managing products with authentication via JWT tokens. The application allows you to create, retrieve, update, and delete products.

JSON Web Tokens (JWTs) are used for securely transmitting information and authenticating users between different applications or services.


#  Installation:

### 1.Clone the Repository:

git clone https://github.com/<C:\Users\bunny\Desktop\interview\ecommerce>/ecommerce-api.git

cd ecommerce-api

### 2.Create and Activate a Virtual Environment:

python -m venv venv

.\venv\Scripts\activate

### 3.Install Dependencies:

pip install -r requirements.txt

### 4.Set Up the Database:

#### 5.Apply migrations:
python manage.py makemigrations

python manage.py migrate

### 6.Create a Superuser:

python manage.py createsuperuser

### 7.Run the Development Server:

python manage.py runserver

# API Endpoints
## Authentication
### Obtain JWT Token:

URL: /api/token/

Method: POST

Request Body:

{

  "username": "<your-username>",

  "password": "<your-password>"

}


Response:

{

  "access": "<access_token>",

  "refresh": "<refresh_token>"

}

### Refresh Token:

URL: /api/token/refresh/

Method: POST

Request Body:

{

  "refresh": "<refresh_token>"

}



# Product Management

## 1.List Products:

URL: /products/

Method: GET

Authentication: Required

Response:

[

  {

    "id": 1,
    "name": "Apple Watch",
    "description": "Apple Watch smart product",
    "imagepath": "/products/apple-watch.jpg",
    "price_unit": "USD",
    "price": 500,
    "manufacturer": "Apple",
    "created": "2025-01-10T12:00:00Z",
    "updated": "2025-01-10T12:00:00Z"

  }

]

## 2.Create a Product:

URL: /products/

Method: POST

Authentication: Required

Request Body:

{

  "name": "Apple Watch",

  "description": "Apple Watch smart product",

  "imagepath": "/products/apple-watch.jpg",

  "price_unit": "USD",

  "price": 500,

  "manufacturer": "Apple"

}

Response:

{

  "id": 1,

  "name": "Apple Watch",

  "description": "Apple Watch smart product",

  "imagepath": "/products/apple-watch.jpg",

  "price_unit": "USD",

  "price": 500,

  "manufacturer": "Apple"

}


### 3.Retrieve a Product by ID:

URL: /products/<id>/

Method: GET

Authentication: Required

### 4.Update a Product:

URL: /products/<id>/

Method: PUT

Authentication: Required

Request Body (not all fields Required):


{

  "name": "Apple Watch",

  "description": "Updated description",

  "imagepath": "/products/apple-watch.jpg",

  "price_unit": "USD",

  "price": 600,

  "manufacturer": "Apple Inc."

}

### 5.Delete a Product:

URL: /products/<id>/

Method: DELETE

Authentication: Required

# Testing APIs

## 1.Using Postman:

Import the API endpoints and make requests using your JWT tokens.

Ensure you include the Authorization: Bearer <access_token> header for secured endpoints.

## 2.Using Django's Admin Panel:

Access the admin panel at /admin/ with your superuser credentials to view and manage products directly.

# Authentication Notes
Install djangorestframework-simplejwt for JWT-based authentication.

Add the following to settings.py:

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ),

}

# Git Process

## 1.Create a GitHub repository.

## 2.Create a develop branch:

git checkout -b develop

## 3.Add your source code to the develop branch:

git add .

git commit -m "Initial commit"

git push origin develop



# API Endpoints
GET /api/products/: List all products


POST /api/products/: Create a new product

GET /api/products/<id>/: Get a product by ID

PUT /api/products/<id>/: Update a product by ID

DELETE /api/products/<id>/: Delete a product by ID



