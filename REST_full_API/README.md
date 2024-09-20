# Implement a RESTful API for E-commerce

Objective: Build a basic API to manage a product catalog and orders for an e-commerce site.

 + Requirements:

    1. Models:
    2. Product: with fields like name, description, price, and stock.
    3. Order: should store products (many-to-many), quantity, and total_price.
    4. API Endpoints:
       + List all products.
       + Create an order (with product, quantity, and total price).
       + Retrieve all orders for a user.
       + Implement basic validation (e.g., order cannot be created if the product is out of stock).

 + Technical Concepts:

    1. Django REST framework
    2. Serialization and Deserialization
    3. URL routing
    4. Django models and ORM
    5. Validations

 + Bonus:

    1. Implement user-specific order history (with authentication).
    2. Add automated tests for the API.
    3. Implement product search with filters (e.g., price range, availability).

