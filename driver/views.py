from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Driver,DriverProfile, Point
# from google.appengine.ext import db

# Create your views here.
def welcome(request):
    return render(request, 'driv.html')


def driver_login(request):
    title = "Uber Clone"

    try:
        if request.method == 'POST':
            form = DriverLogin(request.POST)
            if form.is_valid:
                phone_number = request.POST.get('phone_number')
                try:
                    found_driver = Driver.objects.get(phone_number=phone_number)
                    return redirect(driver, found_driver.id)
                except ObjectDoesNotExist:
                    raise Http404()
            else:
                messages.error(request, ('Please correct the error below.'))
        else:
            form = DriverLogin()
            return render(request, 'registration/driver/login.html',{"title":title,"form":form})
    except ObjectDoesNotExist:
        return redirect(new_driver)


def driver_profile(request, passenger_id, driver_profile_id):
    passengers = Passenger.objects.all()

    try:

        passenger = Passenger.objects.get(id=passenger_id)

        if passenger in passengers:
            driver_profile = DriverProfile.objects.get(id=driver_profile_id)
            title = f'{driver_profile.driver.first_name} {driver_profile.driver.last_name}\'s Profile'
            reviews = DriverReview.get_driver_reviews(driver_profile_id)
            form = ReviewDriverForm()

            return render(request, "all-passengers/driver-profile.html", {"title":title, "passenger":passenger, "driver_profile":driver_profile, "reviews":reviews, "form":form})

        else:

            return redirect(passenger_login)

    except ObjectDoesNotExist:
        return redirect(new_passenger)


def driver(request,id):
    passengers = Passenger.objects.all()

    try:

        passenger = Passenger.objects.get(id=id)
        if passenger in passengers:

            title = "Driver Reviews"

            driver_profiles = DriverProfile.objects.all()

            return render(request, "all-passengers/reviews.html", {"title":title,"passenger":passenger, "driver_profiles":driver_profiles})
        else:

            return redirect(passenger_login)

    except ObjectDoesNotExist:
        return redirect(new_passenger)
