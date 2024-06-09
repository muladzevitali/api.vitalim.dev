from django.contrib import admin

from .models import Location, GeoLocationDistances


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name_geo', 'zone_id', 'sector_id', 'latitude', 'longitude')


@admin.register(GeoLocationDistances)
class GeoLocationDistancesAdmin(admin.ModelAdmin):
    list_display = ('origin_zone_id', 'origin_name_geo', 'dest_zone_id', 'dest_name_geo', 'distance', 'duration')
