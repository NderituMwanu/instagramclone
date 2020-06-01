from django.test import TestCase
from .models import Profile, User


# Create your tests here.
class User(TestCase):
    def setUp(self):
        self.user1=User(author='user1', image="default.jpg", caption="sample", post_date="12-03-2020", location="nairobi", email="sample@mail.com")

    # Testing the instance
    def test_instance(self):
        self.assertTrue(isinstance(self.user1,User))

    #Testing the save method
    def test_save_method(self):
        self.post.save_image()

    #Testing the delete method
    def test_delete_method(self):
        self.post.delete_image()


class Profile(TestCase):
    def setUp(self):
        self.User1=User(Username="sampe",bio="sample bio")

    def test_save_profile_method():
        self.profile.save_profile()