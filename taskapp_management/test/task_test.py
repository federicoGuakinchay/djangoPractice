from django.test import TestCase
from taskapp.models import Task, Importance_task
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date, timedelta
from django.utils import timezone

class TaskModelTest(TestCase):

    def setUp(self):
        # Create a User instance
        self.user = User.objects.create_user(username="testuser", password="password")

        # Create an Importance_task instance
        self.importance_task = Importance_task.objects.create(
            importance="Medium Priority",
            importance_value=3
        )

        # Create a Task instance
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            created_by=self.user,
            iportance_task=self.importance_task,  # Make sure you correct the typo in the model name
            create_task=timezone.now().date(),
            limit_date=timezone.now().date() + timedelta(days=10),
            completed=False
        )

    def test_task_creation(self):
        # Ensure the Task object is created correctly
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.description, "This is a test task")
        self.assertEqual(self.task.created_by, self.user)
        self.assertEqual(self.task.iportance_task.importance, "Medium Priority")
        self.assertFalse(self.task.completed)

    def test_task_str(self):
        # Test the __str__ method
        self.assertEqual(str(self.task), "Test Task")

    def test_task_limit_date_validation(self):
        # Set a limit date in the past and ensure validation fails
        self.task.limit_date = date.today() - timedelta(days=1)
        with self.assertRaises(ValidationError):
            self.task.clean()

    def test_task_limit_date_future(self):
        # Set a limit date in the future and ensure validation passes
        self.task.limit_date = date.today() + timedelta(days=5)
        try:
            self.task.clean()
        except ValidationError:
            self.fail("Task.clean() raised ValidationError unexpectedly!")