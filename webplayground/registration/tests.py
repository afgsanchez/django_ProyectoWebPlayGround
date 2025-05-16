from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        # Create a user instance
        User.objects.create_user('test', 'test@test.com', 'test1234')

    def test_profile_exists(self):
        # Check if the profile was created successfully
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)
