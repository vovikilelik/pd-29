from datetime import date

from ads.models import User, Ad, Category
from users.serializers.user_serializer import UserSerializer


def create_user_model(data_dict) -> User:
    valid_data = {}

    if 'id' in data_dict:
        valid_data['id'] = data_dict['id']

    valid_data['first_name'] = data_dict['first_name']
    valid_data['last_name'] = data_dict['last_name']
    valid_data['username'] = data_dict['username']
    # valid_data['password'] = data_dict['password']
    valid_data['role'] = data_dict['role']
    valid_data['age'] = data_dict['age']

    valid_data['email'] = f"{data_dict['username']}@mail.ru"
    valid_data['birth_date'] = date(1990, 1, 1)

    user = UserSerializer().create(valid_data)
    user.set_password(data_dict['password'])
    user.save()

    if 'locations' in data_dict:
        user.locations.set(data_dict['locations'])

    return user


def create_ad_model(data_dict) -> Ad:
    ad = Ad()

    if 'id' in data_dict:
        ad.id = data_dict['id']

    ad.name = data_dict['name']
    ad.price = data_dict['price']
    ad.description = data_dict['description']
    ad.is_published = data_dict['is_published'] == 'TRUE'

    ad.image = data_dict['image']

    ad.author = User.objects.get(pk=data_dict['author_id'])
    ad.category = Category.objects.get(pk=data_dict['category_id'])

    return ad
