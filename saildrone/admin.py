from django.contrib.gis import admin
from django.contrib.gis.db import models as geomodels
from mapwidgets.widgets import GooglePointFieldWidget

from .models import Drone, Route, Station


@admin.register(Drone)
class DroneAdmin(admin.ModelAdmin):
    list_display = ('location', 'launch_time', 'id')
    search_fields = ('location', 'launch_time', 'id')


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
	list_display = ('route', 'id')
	search_fields = ('route', 'id')


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
	list_display = ('location', 'name')
	search_fields = ('location', 'name')
