from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request


class CategoryIdFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request: Request, queryset, view):

        if 'category_id' not in request.query_params:
            return queryset

        return queryset.filter(category=request.query_params['category_id'])
