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

# NMI = 1852.0

# def update_location(request):
    # '''Store the vehicle location to DB'''
    # if not request.GET.has_key('lat') or not request.GET.has_key('lon') or not request.GET.has_key('utc') \
    #     or not request.GET.has_key('spkn') or not request.GET.has_key('id'):
    #     return HttpResponse("Error!!! Please supply correct parameters : latitude, longitude, time, speed, id", "text/html")
    #
    # lat = request.GET.get('lat', None)
    # northsouth = request.GET.get('ns', None)
    #
    # latitude = None
    # if lat != None:
    #     latitude = float(lat[0:2]) + float(lat[2:])/60.0
    #
    # if northsouth == 's' and latitude:
    #     latitude = latitude * -1.00
    #
    # lng = request.GET.get('lon', None)
    # eastwest = request.GET.get('ew', None)
    #
    # longitude = None
    #
    # if (lng != None):
    #     longitude = float(lng[0:3]) + float(lng[3:])/60.0
    #
    # if ((eastwest == 'w' or eastwest == 'W')) and longitude != None:
    #     longitude = longitude * -1.00
    #
    # utc_date = request.GET.get('date', None)
    # utc_time = request.GET.get('utc', None)
    #
    # spkn = request.GET.get('spkn', None)
    # speed = 0.0
    #
    # if spkn != None :
    #     speed =float(spkn)*NMI/1000.0
    #
    # vehicleid = request.GET.get('id', None)
    # timestamp = datetime.datetime.now()
    #
    # if utc_date != None:
    #     year    = 2000 + int(utc_date[4:])
    #     month   = int(utc_date[2:4])
    #     day     = int(utc_date[0:2])
    #     hour    = int(utc_time[0:2])
    #     minute  = int(utc_time[2:4])
    #     sec     = int(utc_time[4:6])
    #
    #     timestamp = datetime.datetime(year, month, day, hour, minute, sec)
    #
    #
    # logging.info('lat: %f, %f, %d, %s, %s' % (latitude, longitude, speed, str(timestamp), vehicleid))
    #
    # #if not latitude or not longitude or not timestamp or not speed or not vehicleid:
    # #    return HttpResponse("Error!!! Please supply correct parameters : latitude:%s, longitude:%s, time:%s, speed:%s, id:%s" %(str(latitude), str(longitude), timestamp, str(speed), vehicleid), "text/html")
    #
    # try:
    #     vloc = VehiclePosition(latitude=latitude, longitude=longitude, when=timestamp, speed=speed, vehicle_id=vehicleid)
    #     vloc.put()
    # except Exception, e:
    #     raise e
    #
    # return HttpResponse("<html><h1>Stored</h1></html>", "text/html")
