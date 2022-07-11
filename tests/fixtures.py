import pytest

from users.models import User


@pytest.fixture
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = "admin"
    password = "admin"

    django_user_model.objects.create_user(
        username=username, password=password, role=User.ADMIN
    )

    response = client.post(
        '/token/',
        {
            'username': username,
            'password': password
        },
        content_type='application/json'
    )

    return response.json()['access']
