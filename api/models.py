from django.db import models

"""
Added custom table names for the models, to avoid having app name in the table names
"""

class RoomRate(models.Model):
  room_id = models.IntegerField(primary_key=True)
  room_name = models.CharField(max_length=100, blank=False)
  default_rate = models.DecimalField(decimal_places=2, max_digits=8)
  discounts = models.ManyToManyField("Discount", related_name="discount", through="DiscountRoomRate")
  
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
    
class Discount(models.Model):
  class DiscountType(models.TextChoices):
    FIXED = "fixed"
    PERCENTAGE = "percentage"
  
  discount_id = models.IntegerField(primary_key=True)
  discount_name = models.CharField(max_length=100, blank=False)
  discount_type = models.CharField(
    max_length=10,
    choices=DiscountType,
    default=DiscountType.FIXED,
    )
  discount_value = models.DecimalField(decimal_places=2, max_digits=8)
  
  class Meta:
    db_table = 'discount'
    
class DiscountRoomRate(models.Model):
  room_rate = models.ForeignKey(RoomRate, on_delete=models.CASCADE)
  discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
  
  class Meta:
    db_table = 'discount_room_rate'