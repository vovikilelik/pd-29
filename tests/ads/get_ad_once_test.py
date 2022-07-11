import pytest


@pytest.mark.django_db
def test_get_ad_once_list(client, ad):
    response = client.get(f"/ads/{ad.pk}/")

    assert response.status_code == 200

    data = response.json()
    assert data['id'] == ad.pk
