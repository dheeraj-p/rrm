from django.http import Http404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import OverriddenRoomRate
from api.serializers import OverriddenRoomRateSerializer


class OverriddenRoomRateList(APIView):
    @swagger_auto_schema(responses={200: OverriddenRoomRateSerializer(many=True)})
    def get(self, request):
        room_rates = OverriddenRoomRate.objects.all()
        serializer = OverriddenRoomRateSerializer(room_rates, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=OverriddenRoomRateSerializer,
        responses={201: OverriddenRoomRateSerializer()},
    )
    def post(self, request):
        serializer = OverriddenRoomRateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OverriddenRoomRateDetail(APIView):
    def get_object(self, id):
        try:
            return OverriddenRoomRate.objects.get(pk=id)
        except OverriddenRoomRate.DoesNotExist:
            raise Http404(f"Can't find overriden rate with id: {id}")

    @swagger_auto_schema(
        operation_description="Fetches Overridden rate by id (not room_id)",
        responses={
            200: OverriddenRoomRateSerializer(),
            404: "Overridden rate not found",
        },
    )
    def get(self, request, id):
        overridden_rate = self.get_object(id)
        serializer = OverriddenRoomRateSerializer(overridden_rate)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=OverriddenRoomRateSerializer,
        responses={
            200: OverriddenRoomRateSerializer(),
            404: "Overridden rate not found",
            400: "Invalid data provided",
        },
    )
    def patch(self, request, id):
        overridden_rate = self.get_object(id)
        if "id" in request.data:
            del request.data["id"]

        serializer = OverriddenRoomRateSerializer(
            overridden_rate, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_description="Delete Overridden rate by id")
    def delete(self, request, id):
        overridden_rate = self.get_object(id)
        overridden_rate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
