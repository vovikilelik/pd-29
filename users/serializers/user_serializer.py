from rest_framework import serializers

from ads.models import Ad
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    locations = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    total_published = serializers.SerializerMethodField(read_only=True, required=False)

    def get_total_published(self, user):
        ads = Ad.objects.filter(author_id=user.id, is_published=True)
        return len(ads)

    class Meta:
        model = User
        fields = '__all__'
