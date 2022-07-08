from rest_framework import serializers

from users.models import Location


class LocationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Location
        fields = '__all__'
