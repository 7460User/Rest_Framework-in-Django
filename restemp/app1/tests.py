from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import EmpModel

class EmpModelTestCase(TestCase):
    def setUp(self):
        # Create sample data for testing
        EmpModel.objects.create(
            name="John Doe",
            email="john@example.com",
            age=30,
            contact=1234567890,
            development="Software Engineer",
            locations="New York",
            sector="IT"
        )

    def test_empmodel_creation(self):
        # Retrieve the object from the database
        emp = EmpModel.objects.get(name="John Doe")
        # Check if the object exists
        self.assertIsNotNone(emp)
        # Check if the object's attributes match the sample data
        self.assertEqual(emp.name, "John Doe")
        self.assertEqual(emp.email, "john@example.com")
        self.assertEqual(emp.age, 30)
        self.assertEqual(emp.contact, 1234567890)
        self.assertEqual(emp.development, "Software Engineer")
        self.assertEqual(emp.locations, "New York")
        self.assertEqual(emp.sector, "IT")

    def test_str_method(self):
        # Retrieve the object from the database
        emp = EmpModel.objects.get(name="John Doe")
        # Check if the __str__ method returns the expected value
        self.assertEqual(str(emp), "John Doe")
