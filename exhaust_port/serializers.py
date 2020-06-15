from rest_framework import serializers
from exhaust_port.models import XWing, DefenceTower
from django.contrib.auth.models import User


class XWingSerializer(serializers.ModelSerializer):
    """
    Class serializer to manage CRUD of objects XWing
    """
    pilot_id = serializers.IntegerField()

    class Meta:
        model = XWing
        fields = ('id', 'pilot_id', 'health', 'cost', 'name', '_coordinates')


class UserSerializer(serializers.ModelSerializer):
    """
    Class serializer to get User objects data
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class XWingCustomizedSerializer(serializers.ModelSerializer):
    """
    Class serializer to get XWing objects data customized
    """
    pilot = serializers.SerializerMethodField()
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = XWing
        fields = ('id', 'name', 'health', 'cost', 'coordinates', 'pilot')

    @staticmethod
    def get_pilot(obj):
        """
        Get the pilot object
        :param obj: XWing object
        :return: User object serialized
        """
        return UserSerializer(obj.pilot).data

    @staticmethod
    def get_coordinates(obj):
        """
        Get coordinates x, y, z
        :param obj: XWing object
        :return: a json object with the coordinates x, y, z
        """
        x, y, z = obj.get_coordinates()
        return {
            'x': x,
            'y': y,
            'z': z
        }


class DefenceTowerSerializer(serializers.ModelSerializer):
    """
    Class serializer to get DefenceTower objects data
    """
    target = serializers.SerializerMethodField()
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = DefenceTower
        fields = ('id', 'sector', 'health', 'cost', 'target', 'coordinates')

    @staticmethod
    def get_target(obj):
        """
        Get the Target object (XWing)
        :param obj: DefenceTower object
        :return: XWing object serialized
        """
        return XWingCustomizedSerializer(instance=obj.target).data if obj.target else None

    @staticmethod
    def get_coordinates(obj):
        """
        Get coordinates x, y, z
        :param obj: DefenceTower object
        :return: a json object with the coordinates x, y, z
        """
        x, y, z = obj.get_coordinates()
        return {
            'x': x,
            'y': y,
            'z': z
        }
