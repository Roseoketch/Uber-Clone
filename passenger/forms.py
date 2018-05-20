from django import forms
from django.contrib.auth.models import User
# from driver.models import Reviews
from .models import Passenger, Location


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

class PassengerProfileForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['profile_pic']

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('review',)

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['current', 'location']
