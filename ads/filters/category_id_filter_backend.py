from functools import reduce

from django.db.models import Q
from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request


def combine(category_ids):
    query = None

    for cid in category_ids:
        if query:
            query |= Q(category=cid)
        else:
            query = Q(category=cid)

    return query


class CategoryIdFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request: Request, queryset, view):
        conditions = combine(request.GET.getlist('category_id'))

        if not conditions or len(conditions) == 0:
            return queryset

        return queryset.filter(conditions)
