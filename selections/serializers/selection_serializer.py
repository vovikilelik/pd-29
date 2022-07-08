from django.core.validators import MinValueValidator
from rest_framework import serializers

from ads.models import Ad
from ads.serializers.ad_serializer import AdSerializer
from selections.models import Selection
from share.api.custom_validators import ValueEnumValidator


class SelectionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = serializers.ListSerializer(child=AdSerializer())

    class Meta:
        model = Selection
        fields = '__all__'
