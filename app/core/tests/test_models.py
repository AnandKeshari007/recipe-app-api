from django.test import TestCase
from django.contrib.auth import get_user_model
from .. import models
from decimal import Decimal


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = "test@example.com"
        password = 'testpass123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        sample_emails = [
            ["test1@EXAMPLE.COM", "test1@example.com"],
            ["Test2@EXAMPLE.COM", "Test2@example.com"],
            ["TEST3@Example.COM", "TEST3@example.com"],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email=email, password='sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email='', password="sample123")

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            email='test213@example',
            password='sample123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test creating a recipe is successful."""
        user = get_user_model().objects.create_user(
            "test@example.com",
            "testpass123",
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title="Sample Recipe",
            time_minutes=5,
            price=Decimal("5.50"),
            description="Sample recipe description",
        )

        self.assertEqual(str(recipe), recipe.title)


