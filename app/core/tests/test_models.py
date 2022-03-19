from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_validation(self):
        
        email = 'test@techverse.com'
        password = 'testpass123'

        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_with_email_normalization(self):
        email = 'test@TECHVERSE.COM'
        password = 'testpass123' 

        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email.lower())

    def test_invalid_email_id(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '1234')

    def test_create_superuser(self):
        email = 'test1@TECHVERSE.COM'
        password = 'testpass123' 
        user = get_user_model().objects.create_superuser(
            email, password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)