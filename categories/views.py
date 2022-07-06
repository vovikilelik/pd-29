from rest_framework.viewsets import ModelViewSet

from ads.models import Category

from categories.serializers.category_serializer import CategorySerializer
from share.api.default_pagination_set import DefaultPaginationSet


class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = DefaultPaginationSet
