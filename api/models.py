from django.db import models

class RoomRate(models.Model):
  room_id = models.IntegerField(primary_key=True)
  room_name = models.CharField(max_length=100, blank=False)
  default_rate = models.DecimalField(decimal_places=2, max_digits=8)
  
  class Meta:
    db_table = 'room_rate'
    
class OverriddenRoomRate(models.Model):
  room_rate = models.ForeignKey(RoomRate, on_delete=models.CASCADE)
  overridden_rate = models.DecimalField(decimal_places=2, max_digits=8)
  stay_date = models.DateField()
  
  class Meta:
    db_table = 'overridden_room_rate'
    constraints = [
      models.UniqueConstraint(fields=['room_rate', 'stay_date'],name='unique_overridden_rate'),
    ]
    