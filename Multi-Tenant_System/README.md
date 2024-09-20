# Create a Multi-Tenant System with Django

Objective: Implement a multi-tenant system where users from different companies can access only their data.

 + Requirements:

    1. Create a Company model and a User model. Each user belongs to one company.
    2. Users from one company should not be able to see the data from another company.
    3. Allow a company admin to invite users and manage users within their company.

 + Technical Concepts:

    1. Django models and ORM (with relationships)
    2. Django’s authentication and permissions
    3. Database design for multi-tenancy (e.g., foreign key relationships)
    4. Context-based query filtering

 + Bonus:

    1. Implement separate subdomains for each company (e.g., company1.myapp.com).
    2. Add support for company-wide settings or themes.
