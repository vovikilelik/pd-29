import pytest

from ads.serializers.ad_serializer import AdSerializer
from share.api.tests import omit, has_allow


@pytest.mark.django_db
def test_create_ad(client, ad, access_token):

    data = omit(AdSerializer(ad).data, 'id')

    response = client.post(
        f"/ads/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION=f'Bearer {access_token}'
    )

    assert response.status_code == 201
    assert has_allow(response.json(), 'id')
