from django.contrib import admin
from .models import Passenger, Location, Reviews

# Register your models here.
admin.site.register(Passenger)
admin.site.register(Location)
admin.site.register(Reviews)
