from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DefaultPaginationSet(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'size'
    page_size = 10
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'page': self.page.number,
            'items': data
        })
