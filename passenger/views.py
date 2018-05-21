from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http  import HttpResponse
from .models import Passenger, Location, Reviews
from driver.models import DriverProfile
# from .forms import UserForm, PassengerProfile, DriverReviewForm, LocationForm
# from annoying.decorators import ajax_request

# Create your views here.
def passenger(request):
    return render(request,'pass.html')


def passenger_profile(request, username):
    user = User.objects.get(username=username)
    profile = PassengerProfile.objects.get(user=user)
    location = Location.objects.get(user=user)

    title = f"{user.username}"
    return render(request, 'passenger/profile.html', {"user":user, "profile":profile, "location":location})

def update_profile(request, username):
    user = User.objects.get(username = username)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = PassengerProfileForm(request.POST, instance=request.user.passengerprofile, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your have been updated successfully!'))
            return HttpResponseRedirect("/passenger/passenger_profile/%s"%user.username)
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance = request.user)
        profile_form = PassengerProfileForm(instance = request.user.passengerprofile)

    title = 'uber clone'
    return render(request, 'passenger/update_profile.html', {"title":title, "user_form": user_form, "profile_form": profile_form})

def find_driver(request):
    drivers = DriverProfile.objects.all()

    title = 'uber clone'
    return render(request, 'passenger/find_driver.html', {"title":title, "drivers":drivers})

def driver_profile(request, driver_id):
    user = User.objects.get(id=driver_id)
    driver_profile = DriverProfile.objects.filter(user=user)

    title = 'uber clone'
    return render(request, 'passenger/driver_profile.html', {"title":title, "profile":driver_profile})

def review_driver(request):
    user = User.objects.get(id=driver_id)
    driver_profile = DriverProfile.objects.filter(user=user)
    pass

@ajax_request
@login_required
def add_comment(request):
    review_text = request.POST.get('review')
    driver_id = request.POST.get('driver_id')
    driver = User.objects.get(id=driver_id)
    commenter_info = {}

    try:
        review = Reviews(review=review_text, user=request.user)
        # comment = Comment(comment=comment_text, user=request.user, post=post)
        print(review)
        review.save()

        username = request.user.username
        profile_url = reverse('profile', kwargs={'username': request.user.username })


        commenter_info = {
            'username': username,
            'review_text': review_text
        }


        result = 1
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'driver_id': driver_id,
        'commenter_info': commenter_info
    }

def update_location(request, username):
    user = User.objects.get(username = username)

    if request.method == 'POST':
        location_form = LocationForm(request.POST, instance=request.user.passenger_location)

        if location_form.is_valid():
            location_form.save()
            messages.success(request, ('You have updated your location.'))
            return HttpResponseRedirect("/passenger/passenger_profile/%s"%user.username)
        else:
            messages.error(request, ('Please correct the error.'))
    else:
        location_form = LocationForm(instance=request.user.passenger_location)

    title = 'uber clone'
    return render(request, 'driver/update_location.html', {"title":title, "form":location_form})

def current_locations(request):
    '''
    template to render the map with markers
    '''

    title = 'Add Pick Up Location'
    return render(request, 'passenger/pick_up.html', {"title":title})
