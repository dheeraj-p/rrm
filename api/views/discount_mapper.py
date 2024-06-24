from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import DiscountRoomRateSerializer


class DiscountMapper(APIView):
    @swagger_auto_schema(
        operation_description="Creates a mapping between a room_rate and discount by their ids",
        request_body=DiscountRoomRateSerializer,
        responses={201: DiscountRoomRateSerializer()},
    )
    def post(self, request):
        serializer = DiscountRoomRateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
