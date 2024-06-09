from django.db import models
from model_utils.models import TimeStampedModel


class Location(TimeStampedModel):
    class TypeEnum(models.TextChoices):
        CITY = 'CITY'
        VILLAGE = 'VILLAGE'

    id = models.AutoField(primary_key=True)
    name_en = models.CharField(max_length=64, null=True, blank=True)
    name_geo = models.CharField(max_length=64)
    country_en = models.CharField(max_length=64)
    country_geo = models.CharField(max_length=64)
    location_type = models.CharField(max_length=64)
    zone_id = models.CharField(max_length=16, null=True, blank=True)
    sector_id = models.CharField(max_length=16, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        db_table = 'locations'

    def __str__(self):
        return f'{self.name_en}'


class GeoLocationDistances(TimeStampedModel):
    origin_zone_id = models.CharField(max_length=16)
    origin_name_geo = models.CharField(max_length=64)
    dest_zone_id = models.CharField(max_length=16)
    dest_name_geo = models.CharField(max_length=64)
    distance = models.FloatField()
    duration = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'geo_locations_distances'

    def __str__(self):
        return f'{self.origin_zone_id} - {self.dest_name_geo}'
