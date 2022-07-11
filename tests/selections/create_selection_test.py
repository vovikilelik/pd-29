import pytest

from ads.serializers.ad_serializer import AdSerializer
from selections.serializers.selection_serializer import SelectionSerializer
from share.api.tests import omit, has_allow


@pytest.mark.django_db
def test_create_selection(client, selection, access_token):

    data = omit(SelectionSerializer(selection).data, 'id')

    response = client.post(
        f"/selections/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION=f'Bearer {access_token}'
    )

    assert response.status_code == 201
    assert has_allow(response.json(), 'id')
