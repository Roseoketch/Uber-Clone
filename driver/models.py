from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from google.appengine.ext import db

# Create your models here.


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver')
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=500, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name()


class DriverProfile(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True,upload_to="driver/profile-pic")
    car_image = models.ImageField(blank=True,upload_to="car-image/",)
    car_capacity = models.PositiveIntegerField(default=0, blank=True)
    car_number_plate = models.CharField(blank=True, max_length=255)
    car_color = models.CharField(max_length=255, blank=True)

# class VehiclePosition(models.Model):
#     latitude = db.FloatProperty()       # Instead can also use GeoPtProperty , but obviously lose ordering based on lat/lng
#     longitude = db.FloatProperty()
#     when = db.DateTimeProperty()
#     speed = db.FloatProperty()
#     vehicle_id= db.StringProperty()
#     create_time = db.DateTimeProperty(auto_now_add = True)
#
#
#     def __str__(self):
#         return "%s - %s" % (self.latitude, self.longitude)
