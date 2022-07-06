from rest_framework import serializers

from ads.models import Ad


class AdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    image = serializers.ImageField()

    class Meta:
        model = Ad
        fields = '__all__'
