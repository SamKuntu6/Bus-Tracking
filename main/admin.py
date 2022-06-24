from django.contrib import admin
from .models import *

 
class TripAdmin(admin.ModelAdmin):
    list_display = ('trip_ref_no', 'updated', 'type')


class RouteAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_address', 'end_address', 'time', 'distance', 'status')


class BussAdmin(admin.ModelAdmin):
    list_display = ('plate_no', 'capacity', 'condition', 'driver_assigned', 'attendant_assigned')


admin.site.register(Trip, TripAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Buss, BussAdmin)
