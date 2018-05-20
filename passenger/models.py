from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Passenger')
    phone = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    profilePic = models.ImageField(upload_to='profile/',null=True,blank=True)
    bio = models.CharField(max_length=60,blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name()

    @receiver(post_save,sender = User)
    def create_user_profile(sender,instance,created, **kwargs):
        if created:
            Passenger.objects.create(user=instance)

    @receiver(post_save,sender = User)
    def save_user_profile(sender,instance,**kwargs):
        instance.passenger.save()



class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='passenger')
    current = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)

    #
    @receiver(post_save,sender = User)
    def create_user_location(sender,instance,created, **kwargs):
        if created:
            Location.objects.create(user=instance)

    @receiver(post_save,sender = User)
    def save_user_location(sender,instance,**kwargs):
        instance.passenger.save()


class Reviews(models.Model):
    review = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='passenger_reviews')
