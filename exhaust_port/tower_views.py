from rest_framework.views import APIView  # is not good import *, only import package or files you will use
from rest_framework import status
from rest_framework.response import Response
from death_star.utils.response_vo import json_data
from exhaust_port.serializers import DefenceTowerSerializer
from exhaust_port.models import XWing, DefenceTower


class DefenceTowerView(APIView):
    """
    Class to manage Defence Tower
    """

    @staticmethod
    def get(request, **kwargs):
        """
        Get the towers list
        :param request: the params of the GET request
        :param kwargs: list of dict that we can use in some cases to send additional params
        :return: :return: a serializer of DefenceTower objects
        """
        data = request.GET
        x_wing_id = data.get('wing_id', False)
        if x_wing_id:  # get towers of the wing
            try:
                x_wing_obj = XWing.objects.get(pk=x_wing_id)
            except XWing.DoesNotExist:
                return Response(json_data(
                    message='XWing doesnt exist',
                    status='danger'
                ), status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            towers = x_wing_obj.towers.all()
        else:  # get all towers
            towers = DefenceTower.objects.all()
        return Response(json_data(
            data=DefenceTowerSerializer(instance=towers, many=True).data
        ), status=status.HTTP_200_OK)

    @staticmethod
    def post(request, **kwargs):
        """
        The pilot of a wing can destroy a tower if he is on target
        :param request: data from the POST request
        :param kwargs: list of dict that we can use in some cases to send additional params
        :return: the message according to the action result
        """
        data = request.data
        tower_id = data.get('tower_id', False)
        pilot_id = data.get('pilot_id', False)
        if not tower_id or not pilot_id:
            return Response(json_data(
                status='danger',
                message='Missing data'
            ), status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        # catch the exception if the wing doesnt exist
        try:
            wing = XWing.objects.get(pilot_id=pilot_id)
        except XWing.DoesNotExist:
            return Response(json_data(
                message='XWing doesnt exist',
                status='danger'
            ), status=status.HTTP_404_NOT_FOUND)
        # catch the exception if the tower doesnt exist
        try:
            tower = DefenceTower.objects.get(pk=tower_id)
        except DefenceTower.DoesNotExist:
            return Response(json_data(
                message='Tower doesnt exist',
                status='danger'
            ), status=status.HTTP_404_NOT_FOUND)
        # catch the exception if the wing is not on target by this tower
        try:
            tower_target_wing = wing.towers.get(pk=tower_id)
        except DefenceTower.DoesNotExist:
            return Response(json_data(
                message='XWing {} is not on target of the tower {}'.format(wing.name, tower),
                status='danger'
            ), status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        # destroy tower
        tower_target_wing.destroy()
        return Response(json_data(
            message='Tower was destroyed',
        ), status=status.HTTP_200_OK)
