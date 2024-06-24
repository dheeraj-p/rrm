from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Discount
from api.serializers import DiscountSerializer

class DiscountList(APIView):
  def get(self, request):
    discounts = Discount.objects.all()
    serializer = DiscountSerializer(discounts, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = DiscountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class DiscountDetail(APIView):
  def get_object(self, discount_id):
    try:
      return Discount.objects.get(pk=discount_id)
    except Discount.DoesNotExist:
      raise Http404(f"Can't find discount with id: {discount_id}")
  
  def get(self, request, discount_id):
    room_rate = self.get_object(discount_id)
    serializer = DiscountSerializer(room_rate)
    return Response(serializer.data)

  def patch(self, request, discount_id):
    room_rate = self.get_object(discount_id)
    if 'discount_id' in request.data:
      return Response({'detail': "Updating discount_id is not allowed"}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = DiscountSerializer(room_rate, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, discount_id):
    room_rate = self.get_object(discount_id)
    room_rate.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)