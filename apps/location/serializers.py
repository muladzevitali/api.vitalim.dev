from rest_framework import serializers

from apps.location.models import Location, GeoLocationDistances


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class GeoLocationDistancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoLocationDistances
        fields = '__all__'
