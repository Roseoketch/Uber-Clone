from django import forms
from django.contrib.auth.models import User
from .models import DriverProfile, Driver, Location, Point

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class DriverProfileForm(forms.ModelForm):
    class Meta:
        model = DriverProfile
        fields = ['profile_pic', 'gender', 'car_capacity', 'plates', 'car_color']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['current', 'location']

class PointForm(forms.ModelForm):
    class Meta:
        model = Point
        fields = ['name', 'location']
