from rest_framework import serializers

from ads.models import Ad
from share.api.custom_validators import AgeAllowValidator, rambler_ban_validator
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    birth_date = serializers.DateField(allow_null=False, validators=[AgeAllowValidator(9)])
    email = serializers.EmailField(validators=[rambler_ban_validator])

    locations = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    total_published = serializers.SerializerMethodField(read_only=True, required=False)

    def get_total_published(self, user):
        ads = Ad.objects.filter(author_id=user.id, is_published=True)
        return len(ads)

    # def create(self, data):
    #     user = super().create(data)
    #
    #     user.set_password(user.password)
    #     user.save()
    #
    #     return user

    class Meta:
        model = User
        fields = '__all__'
