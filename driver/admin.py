from django.contrib import admin
from .models import Driver, DriverProfile, Point

# Register your models here.
admin.site.register(Driver)
admin.site.register(DriverProfile)
admin.site.register(Point)
