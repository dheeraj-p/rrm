from django.http import Http404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import RoomRate
from api.serializers import RoomRateSerializer


class RoomRateList(APIView):
    @swagger_auto_schema(responses={200: RoomRateSerializer(many=True)})
    def get(self, request):
        room_rates = RoomRate.objects.all()
        serializer = RoomRateSerializer(room_rates, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=RoomRateSerializer,
        responses={201: RoomRateSerializer()},
    )
    def post(self, request):
        serializer = RoomRateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomRateDetail(APIView):
    def get_object(self, room_id):
        try:
            return RoomRate.objects.get(pk=room_id)
        except RoomRate.DoesNotExist:
            raise Http404(f"Can't find room rate with room id: {room_id}")

    @swagger_auto_schema(
        responses={200: RoomRateSerializer(), 404: "Room rate not found"},
    )
    def get(self, request, room_id):
        room_rate = self.get_object(room_id)
        serializer = RoomRateSerializer(room_rate)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "room_name": {"type": openapi.TYPE_STRING},
                "default_rate": {"type": openapi.TYPE_NUMBER},
            },
        ),
        responses={
            200: RoomRateSerializer(),
            404: "Room rate not found",
            400: "Invalid data provided",
        },
    )
    def patch(self, request, room_id):
        room_rate = self.get_object(room_id)
        if "room_id" in request.data:
            del request.data["room_id"]

        serializer = RoomRateSerializer(room_rate, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, room_id):
        room_rate = self.get_object(room_id)
        room_rate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
