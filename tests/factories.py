import factory.django

from ads.models import Ad, Category
from selections.models import Selection
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = "test"
    password = "pass"


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Category

    name = "Category 1"
    slug = "slug"


class AdFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Ad

    name = "Test any ad"
    price = 0
    description = ""
    is_published = False

    image = None

    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)


def ad_iterator():
    yield factory.SubFactory(AdFactory)


class SelectionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Selection

    name = "Test Selection"
    owner = factory.SubFactory(UserFactory)
    items = factory.RelatedFactoryList(AdFactory)
