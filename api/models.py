from django.db import models

class RoomRate(models.Model):
  room_id = models.IntegerField(primary_key=True)
  room_name = models.CharField(max_length=100, blank=False)
  default_rate = models.DecimalField(decimal_places=2, max_digits=8)
  
  class Meta:
    db_table = 'room_rate'

