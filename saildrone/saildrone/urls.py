from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

# from . import views


urlpatterns = [
  #   url(r'^stations/$',
  #       views.StationListView.as_view(),
  #       name='station-list'),
  #  	url(r'^stations/(?P<pk>[^/.]+)/$',
  #       views.StationView.as_view(),
  #       name='station-detail'),

  #  	url(r'^drones/$',
  #       views.DroneListView.as_view(),
  #       name='drone-list'),
 	# url(r'^drones/(?P<pk>[^/.]+)/$',
  #       views.DroneView.as_view(),
  #       name='drone-detail'),

  #  	url(r'^routes/$',
  #       views.RouteListView.as_view(),
  #       name='route-list'),
  #  	url(r'^routes/(?P<pk>[^/.]+)/$',
  #       views.RouteView.as_view(),
  #       name='route-detail'),

   	url(r'^admin/', admin.site.urls),
]


# urlpatterns = format_suffix_patterns(urlpatterns)