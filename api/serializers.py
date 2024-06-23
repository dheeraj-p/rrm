from rest_framework import serializers
from .models import RoomRate

class RoomRateSerializer(serializers.ModelSerializer):
  class Meta:
    model = RoomRate
    fields = ['room_id', 'room_name', 'default_rate']