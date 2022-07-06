from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request


class PriceFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request: Request, queryset, view):

        if 'price_from' not in request.query_params or 'price_to' not in request.query_params:
            return queryset

        return queryset.filter(price__range=[request.query_params['price_from'], request.query_params['price_to']])
