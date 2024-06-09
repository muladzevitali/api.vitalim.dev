from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.location import serializers
from apps.location.models import Location, GeoLocationDistances


class LocationFilters(filters.FilterSet):
    zone_id = filters.CharFilter(field_name='zone_id', lookup_expr='exact')
    sector_id = filters.CharFilter(field_name='sector_id', lookup_expr='exact')
    name_en = filters.CharFilter(field_name='name_en', lookup_expr='icontains')
    name_geo = filters.CharFilter(field_name='name_geo', lookup_expr='contains')

    class Meta:
        model = Location
        fields = ['zone_id', 'sector_id', 'name_en', 'name_geo']


class LocationDistanceFilters(filters.FilterSet):
    origin_zone_id = filters.CharFilter(field_name='origin_zone_id')
    origin_name_geo = filters.CharFilter(field_name='origin_name_geo')
    dest_zone_id = filters.CharFilter(field_name='dest_zone_id')
    dest_name_geo = filters.CharFilter(field_name='dest_name_geo')

    class Meta:
        model = GeoLocationDistances
        fields = ['origin_zone_id', 'origin_name_geo', 'dest_zone_id', 'dest_name_geo']


class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = serializers.LocationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LocationFilters


class LocationDistanceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GeoLocationDistances.objects.all()
    serializer_class = serializers.GeoLocationDistancesSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LocationDistanceFilters
