import pytest

from exhaust_port.models import XWing, DefenceTower


@pytest.fixture
def x_wing(admin_user):
    """
    create Xwing text
    """
    return XWing.objects.create(pilot=admin_user, cost=13331.33, name="random_name", _coordinates="20305")


@pytest.fixture
def defence_tower(x_wing):
    """
    create DefenceTower object
    """
    return DefenceTower.objects.create(
        sector='a1', health=50, cost=10.0, _coordinates='20202', target=x_wing
    )


@pytest.mark.django_db
class TestXWing:

    def test_is_destroyed(self, x_wing):
        assert x_wing.is_destroyed(100)
        assert not x_wing.is_destroyed(99)
