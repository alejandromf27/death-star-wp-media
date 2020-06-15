import pytest
from rest_framework import status
from exhaust_port.models import XWing, DefenceTower


@pytest.mark.django_db
class TestGetDefenceTower:

    @staticmethod
    def test_get(client, admin_user):
        """
        method to test GET towers of a wing
        """
        wing = XWing.objects.create(pilot=admin_user, cost=13331.33, name="random_name", _coordinates="20305")
        DefenceTower(
            sector='a1', health=50, cost=10.0, _coordinates='20202', target=wing
        )
        response = client.get('/exhaust_port/towers/?wing_id=' + str(wing.id))
        assert response.status_code == status.HTTP_200_OK

    @staticmethod
    def test_post(client, admin_user):
        """
        method to test if a pilot can destroy a tower when it is targeting the pilot's wing
        """
        wing = XWing.objects.create(pilot=admin_user, cost=13331.33, name="random_name", _coordinates="20305")
        tower = DefenceTower.objects.create(
            sector='a1', health=50, cost=10.0, _coordinates='20202', target=wing
        )
        response = client.post('/exhaust_port/towers/', data={
            'tower_id': tower.id,
            'pilot_id': admin_user.id
        }, content_type='application/json')
        assert response.status_code == status.HTTP_200_OK
