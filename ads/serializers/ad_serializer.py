from django.core.validators import MinValueValidator
from rest_framework import serializers

from ads.models import Ad
from share.api.custom_validators import ValueEnumValidator


class AdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    price = serializers.FloatField(validators=[MinValueValidator(0)])
    is_published = serializers.BooleanField(validators=[ValueEnumValidator(False)])
    description = serializers.CharField(allow_blank=True)

    class Meta:
        model = Ad
        fields = '__all__'
