from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='passenger')
    phone = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    profilePic = models.ImageField(upload_to='profile/',null=True,blank=True)
    bio = models.CharField(max_length=60,blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name()
