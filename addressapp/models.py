from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=128)
    repassword = models.CharField(max_length=128)   # Store the hashed password
    photo = models.ImageField(upload_to='images/',default='manasa.jpeg')
    username = models.CharField(max_length=255)

    
    def __str__(self):
        return self.username
    
class UserContact(models.Model):
    email = models.EmailField()
    address=models.TextField()
    username = models.CharField(max_length=255, blank=True)
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE,default='')
    def __str__(self):
        return self.username
# Any other models you might have in your app can be defined here.
