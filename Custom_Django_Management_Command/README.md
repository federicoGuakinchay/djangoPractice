# Create a Custom Django Management Command

Objective: Write a custom management command to perform scheduled maintenance on your database.

 + Requirements:

    1. Write a management command that:
         + Archives old data (e.g., moves records older than a certain date to an archive).
         + Deletes old logs or temporary data.
         + Schedule the command to run automatically (e.g., using cron or Django Celery).

 + Technical Concepts:

    1. Django management commands
    2. Django ORM for bulk updates
    3. Scheduling tasks with cron or Celery

 + Bonus:

    1. Provide a report of the operation (e.g., number of records archived or deleted).
    2. Implement unit tests for the management command.
