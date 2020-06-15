from rest_framework.views import APIView  # is not good import *, only import package or files you will use
from rest_framework import status
from rest_framework.response import Response
import traceback
from death_star.utils.response_vo import json_data
from exhaust_port.serializers import XWingSerializer, XWingCustomizedSerializer
from exhaust_port.models import XWing


class XWingList(APIView):  # PEP8 class names CapWords convention
    """
    class to manage x wings
    """

    @staticmethod
    def get(request, **kwargs):  # we need to use static methods (not self param) if we are not going to use it
        """
        Get the list of x wings
        :param request: the params of the GET request
        :param kwargs: list of dict that we can use in some cases to send additional params
        :return: a serializer of XWing objects
        """
        # retrieve all wings
        x_winds = XWing.objects.all().order_by('name')
        # Is a good practice return serialized objects using the same response VO, you can use json lib but i prefer
        # customize the json response in a standard VO (json_data)
        return Response(json_data(
            data=XWingCustomizedSerializer(instance=x_winds, many=True).data
        ), status=status.HTTP_200_OK)

    @staticmethod
    def post(request, **kwargs):  # we need to use static methods (not self param) if we are not going to use it
        """
        Create a wing
        :param request: the data from the POST request
        :param kwargs: list of dict that we can use in some cases to send additional params
        :return: the serializer XWing object created
        """
        # Is a good practice use serialized objects for POST to save simple objects
        data = request.data
        # validate correct coordinates format , if not the function get_coordinates on XWing object doesnt work
        if not XWingList.validate_coordinates(data.get('_coordinates', '')):
            return Response(json_data(
                status='danger',
                message='Coordinates format is wrong. Format is three numbers separated by 0, Ex: 12034045'
            ), status=status.HTTP_400_BAD_REQUEST)
        try:
            serializer = XWingSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(json_data(serializer.data), status=status.HTTP_201_CREATED)
            return Response(json_data(
                status='danger',
                message=serializer.errors
            ), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            traceback.print_exc()
            return Response(json_data(
                message=str(e),
                status='danger'
            ), status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request, **kwargs):
        """
        Update a wing
        :param request: the data from the PUT request
        :param kwargs: list of dict that we can use in some cases to send additional params
        :return: the serializer XWing object updated
        """
        # Is a good practice use serialized objects for POST to save simple objects
        data = request.data
        if data.get('_coordinates', False):
            if not XWingList.validate_coordinates(data['_coordinates']):
                return Response(json_data(
                    status='danger',
                    message='Coordinates format is wrong. Format is three numbers separated by 0, Ex: 12034045'
                ), status=status.HTTP_400_BAD_REQUEST)
        try:
            wing = XWing.objects.get(pk=data['id'])
        except XWing.DoesNotExist:
            return Response(json_data(
                status='danger',
                message='Record Not Found'
            ), status=status.HTTP_404_NOT_FOUND)
        try:
            serializer = XWingSerializer(wing, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(json_data(
                    data=serializer.data
                ), status=status.HTTP_201_CREATED)
            return Response(json_data(
                message=serializer.errors,
                status='danger'
            ), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(json_data(
                message=str(e),
                status='danger'
            ), status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        try:
            wing = XWing.objects.get(pk=request.data['id'])
        except XWing.DoesNotExist:
            return Response(json_data(
                status='danger',
                message='Record Not Found'
            ), status=status.HTTP_404_NOT_FOUND)
        wing.delete()
        return Response(json_data(
            message='CONTENT DELETED'
        ), status=status.HTTP_200_OK)

    @staticmethod
    def validate_coordinates(coordinates):
        # validate correct coordinates format , if not the function get_coordinates on XWing object doesnt work
        lst = list(filter(lambda x: x != '', coordinates.split('0')))
        if len(lst) != 3 or not coordinates.isnumeric():
            return False
        return True
