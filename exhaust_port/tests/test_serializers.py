import pytest
from rest_framework.exceptions import ValidationError
from exhaust_port.models import XWing
from exhaust_port.serializers import XWingSerializer


class TestWingSerializer:

    @staticmethod
    def test_expected_serialized_json(admin_user):
        expected_results = {
            'id': 1,
            'pilot_id': admin_user.id,
            'health': 80,
            'cost': 123.4,
            'name': 'Wing1',
            '_coordinates': '10101'
        }
        wing = XWing(**expected_results)
        results = XWingSerializer(wing).data
        assert results == expected_results

    # @staticmethod
    # def test_raise_error_when_missing_required_field():
    #     incomplete_data = {
    #         'id': 1,
    #         'health': 80,
    #         'cost': 123.4,
    #         'name': 'Wing12'
    #     }
    #     serializer = XWingSerializer(data=incomplete_data)
    #     with pytest.raises(ValidationError):
    #         serializer.is_valid(raise_exception=True)
