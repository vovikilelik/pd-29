import pytest

from ads.models import Ad
from share.api.tests import has_allow


@pytest.mark.django_db
def test_get_ads_list(client, ad):
    response = client.get(f"/ads/")

    assert response.status_code == 200

    data = response.json()
    assert has_allow(data, 'items', 'total')
    assert data['total'] == len(Ad.objects.all())
