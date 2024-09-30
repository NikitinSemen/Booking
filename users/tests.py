from django.test import TestCase
from users.models import User


class UserModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='testuser@example.com',
            password='password123',
            first_name='Test',
            last_name='User'
        )

    def test_user_string_representation(self):
        self.assertEqual(str(self.user), 'Test')

    def test_user_email_field(self):
        self.assertEqual(self.user.email, 'testuser@example.com')


