from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from locations.models import Location
from locations.serializers.location_serializer import LocationSerializer
from share.api.default_pagination_set import DefaultPaginationSet


class LocationsViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    pagination_class = DefaultPaginationSet
