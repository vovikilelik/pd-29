from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request


class LocationFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request: Request, queryset, view):

        if 'location' not in request.query_params:
            return queryset

        return queryset.filter(author__locations__name__contains=request.query_params['location'])
