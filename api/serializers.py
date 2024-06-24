from rest_framework import serializers
from api import models

class RoomRateSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.RoomRate
    fields = ['room_id', 'room_name', 'default_rate']
    
class OverriddenRoomRateSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.OverriddenRoomRate
    fields = ['room_rate', 'overridden_rate', 'stay_date', 'id']
    validators = [
      serializers.UniqueTogetherValidator(
        queryset= models.OverriddenRoomRate.objects.all(),
        fields=['room_rate', 'stay_date'],
        message=("Room rate can be overridden only one for a specific date."
                 "There is already a overridden rate for this room id and date"),
        ),
      ]