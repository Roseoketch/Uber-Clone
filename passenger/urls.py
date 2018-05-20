from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # url('^$',views.passenger,name = 'passenger'),
    url(r'^passenger/(\d+)',views.passenger,name ='passenger'),
    url(r'^passenger_profile/(?P<username>[-_\w.]+)/update/$', views.update_profile, name='update_profile'),
    url(r'^drivers/$', views.find_driver, name='find_driver'),
    url(r'^driver/profile/(\d+)$', views.driver_profile, name='driver_profile'),
    url(r'^driver/(\d+)/review/$', views.review_driver, name='review_driver'),
    url(r'^driver/profile/comment/$', views.add_comment, name='comment'),
    url(r'^location/(?P<username>[-_\w.]+)/update/$', views.update_location, name='update_location_view'),
    url(r'^pickup_locations/$', views.pickup_locations, name='pickup_locations'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
