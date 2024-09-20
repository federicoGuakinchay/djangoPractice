# Build a Custom Middleware for Request Logging

Objective: Create a custom Django middleware to log details about incoming HTTP requests.

 + Requirements:

    1. Log the request method, path, user (if authenticated), and time taken to process the request.
    2. Store the log in a file, database, or send it to an external logging service.
    3. Allow certain paths to be excluded from logging (e.g., static files or media).

 + Technical Concepts:

    1. Django middleware
    2. Working with request/response cycle
    3. Logging in Django
    4. Django settings

 + Bonus:

    1. Add filtering based on request methods (e.g., log only POST/PUT requests).
    2. Include error handling and exception logging.

       
