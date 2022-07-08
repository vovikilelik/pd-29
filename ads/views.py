from django.http import JsonResponse, HttpResponse

# Create your views here.
from django.views import View
from rest_framework.filters import SearchFilter
from rest_framework.generics import UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from ads.filters.category_id_filter_backend import CategoryIdFilterBackend
from ads.filters.location_filter_backend import LocationFilterBackend
from ads.filters.price_filter_backend import PriceFilterBackend
from ads.models import Ad, Category
from ads.serializers.ad_serializer import AdSerializer
from ads.serializers.category_serializer import CategorySerializer
from share.api.default_pagination_set import DefaultPaginationSet
from share.api.permissions import create_custom_action_permission, IsAuthenticatedOrAdmin
from users.models import User


class IsOwner(IsAuthenticatedOrAdmin):

    def has_object_permission(self, request, view, obj):
        if obj.author_id == request.user.id:
            return True

        return request.user.role == User.ADMIN


class AdsViewSet(ModelViewSet):
    queryset = Ad.objects.all()

    serializer_class = AdSerializer
    pagination_class = DefaultPaginationSet
    filter_backends = [PriceFilterBackend, CategoryIdFilterBackend, LocationFilterBackend, SearchFilter]
    permission_classes = [create_custom_action_permission(IsOwner, actions=['update', 'destroy'])]

    search_fields = ['name', 'description']


class AdImageUpload(UpdateAPIView):
    model = Ad
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        ad = self.get_object()

        ad.image = request.FILES["image"]
        ad.save()

        return JsonResponse(AdSerializer(ad).data)


class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = DefaultPaginationSet

