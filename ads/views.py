from django.http import JsonResponse, HttpResponse

# Create your views here.
from django.views import View
from rest_framework.filters import SearchFilter
from rest_framework.generics import UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from ads.filters.category_id_filter_backend import CategoryIdFilterBackend
from ads.filters.location_filter_backend import LocationFilterBackend
from ads.filters.price_filter_backend import PriceFilterBackend
from ads.models import Ad
from ads.serializers.ad_serializer import AdSerializer
from share.api.default_pagination_set import DefaultPaginationSet


class Hello(View):

    def get(self, request):
        # convert_models()

        return HttpResponse('ok', status=200)


class AdsViewSet(ModelViewSet):
    queryset = Ad.objects.all()

    serializer_class = AdSerializer
    pagination_class = DefaultPaginationSet
    filter_backends = [PriceFilterBackend, CategoryIdFilterBackend, LocationFilterBackend, SearchFilter]

    search_fields = ['name', 'description']


class AdImageUpload(UpdateAPIView):
    model = Ad
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        ad = self.get_object()

        ad.image = request.FILES["image"]
        ad.save()

        return JsonResponse(AdSerializer(ad).data)
