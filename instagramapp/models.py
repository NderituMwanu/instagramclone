from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default = "1")
    # profile = models.ForeignKey('profile.User',on_delete=models.CASCADE, default = "1")
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField(default="2")
    post_date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length =30, default="Nairobi,Kenya")
    email = models.EmailField(default="sample@gmail.com")
    
    def __str__(self):
        return self.caption

    def save_image(self):
        self.save()

    def delete_image(self):
        self.deleter()
    


class Profile(models.Model):
    username = models.CharField(max_length =30)
    bio = models.CharField(max_length =30)
    profile_picture = models.ImageField(blank=True, null=True)
    followers = models.CharField(max_length =20)
    following = models.CharField(max_length =20)
    posts = models.CharField(max_length = 20)

    def __str__(self):
        return self.username

