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
    
class DiscountSerializer(serializers.ModelSerializer):
  def validate(self, attrs):
    """
    Validates that discount value is correct for Fixed and Percentage.
    """
    if attrs['discount_type'] == 'fixed':
      return attrs
    
    if attrs['discount_value'] > 100.0:
      raise serializers.ValidationError("Discount value can't be more than 100%")
    
    return attrs
  class Meta:
    model = models.Discount
    fields = ['discount_id', 'discount_name', 'discount_type', 'discount_value']