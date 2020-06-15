import pytest
from rest_framework import status
from exhaust_port.models import XWing


@pytest.mark.django_db
class TestGetXWings:

    @staticmethod
    def test_get(client):
        """
        method to test the GET list of wings
        """
        response = client.get('/exhaust_port/x_wings/', content_type='application/json')
        assert response.status_code == status.HTTP_200_OK

    @staticmethod
    def test_post(client, admin_user):
        """
        method to test the creation of a wing (POST)
        """
        response = client.post('/exhaust_port/x_wings/', data={
            'pilot_id': admin_user.id,
            'health': 80,
            'cost': 123.4,
            'name': 'Wing1',
            '_coordinates': '10101'
        }, content_type='application/json')
        assert response.status_code == status.HTTP_201_CREATED

    @staticmethod
    def test_put(client, admin_user):
        """
        method to test the wing edition (PUT)
        """
        wing = XWing.objects.create(pilot=admin_user, cost=13331.33, name="random_name", _coordinates="20305")
        response = client.put('/exhaust_port/x_wings/', data={
            'id': wing.id,
            'pilot_id': admin_user.id,
            'health': 80,
            'cost': 123.4,
            'name': 'Wing1',
            '_coordinates': '10101'
        }, content_type='application/json')
        assert response.status_code == status.HTTP_201_CREATED

    @staticmethod
    def test_delete(client, admin_user):
        wing = XWing.objects.create(pilot=admin_user, cost=13331.33, name="random_name", _coordinates="20305")
        response = client.delete('/exhaust_port/x_wings/', data={
            'id': wing.id
        }, content_type='application/json')
        assert response.status_code == status.HTTP_200_OK
