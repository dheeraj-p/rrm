from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api import models, serializers

class RoomRateList(APIView):
  def get(self, request):
    room_rates = models.RoomRate.objects.all()
    serializer = serializers.RoomRateSerializer(room_rates, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = serializers.RoomRateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class RoomRateDetail(APIView):
  def get_object(self, room_id):
    try:
      return models.RoomRate.objects.get(pk=room_id)
    except models.RoomRate.DoesNotExist:
      raise Http404(f"Can't find room rate with room id: {room_id}")
  
  def get(self, request, room_id):
    room_rate = self.get_object(room_id)
    serializer = serializers.RoomRateSerializer(room_rate)
    return Response(serializer.data)

  def patch(self, request, room_id):
    room_rate = self.get_object(room_id)
    if 'room_id' in request.data:
      return Response({'detail': "Updating room_id is not allowed"}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = serializers.RoomRateSerializer(room_rate, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, room_id):
    room_rate = self.get_object(room_id)
    room_rate.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class OverriddenRoomRateList(APIView):
  def get(self, request):
    room_rates = models.OverriddenRoomRate.objects.all()
    serializer = serializers.OverriddenRoomRateSerializer(room_rates, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = serializers.OverriddenRoomRateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class OverriddenRoomRateDetail(APIView):
  def get_object(self, id):
    try:
      return models.OverriddenRoomRate.objects.get(pk=id)
    except models.OverriddenRoomRate.DoesNotExist:
      raise Http404(f"Can't find overriden rate with id: {id}")
  
  def get(self, request, id):
    overridden_rate = self.get_object(id)
    serializer = serializers.OverriddenRoomRateSerializer(overridden_rate)
    return Response(serializer.data)

  def patch(self, request, id):
    overridden_rate = self.get_object(id)
    if 'id' in request.data:
      del request.data['id']
    
    serializer = serializers.OverriddenRoomRateSerializer(overridden_rate, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, id):
    overridden_rate = self.get_object(id)
    overridden_rate.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)