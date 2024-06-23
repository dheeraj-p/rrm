from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import RoomRate
from api.serializers import RoomRateSerializer

class RoomRateList(APIView):
  def get(self, request):
    snippets = RoomRate.objects.all()
    serializer = RoomRateSerializer(snippets, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = RoomRateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
