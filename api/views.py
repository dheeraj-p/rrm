from django.http import Http404
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
  

class RoomRateDetail(APIView):
  def get_object(self, room_id):
    try:
      return RoomRate.objects.get(pk=room_id)
    except RoomRate.DoesNotExist:
      raise Http404(f"Can't find room rate with room id: {room_id}")
  
  def get(self, request, room_id):
    room_rate = self.get_object(room_id)
    serializer = RoomRateSerializer(room_rate)
    return Response(serializer.data)

  def patch(self, request, room_id):
    room_rate = self.get_object(room_id)
    if 'room_id' in request.data:
      return Response({'detail': "Updating room_id is not allowed"}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = RoomRateSerializer(room_rate, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, room_id):
    room_rate = self.get_object(room_id)
    room_rate.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
