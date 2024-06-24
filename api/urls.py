from django.urls import path

from api.views import discount, overridden_rate, room_rate, discount_mapper, lowest_rate

urlpatterns = [
    path("room_rates", room_rate.RoomRateList.as_view()),
    path("room_rates/<int:room_id>", room_rate.RoomRateDetail.as_view()),
    path("overridden_rates", overridden_rate.OverriddenRoomRateList.as_view()),
    path(
        "overridden_rates/<int:id>",
        overridden_rate.OverriddenRoomRateDetail.as_view(),
    ),
    path("discounts", discount.DiscountList.as_view()),
    path("discounts/<int:discount_id>", discount.DiscountDetail.as_view()),
    path("add-discount", discount_mapper.DiscountMapper.as_view()),
    path("lowest-rate", lowest_rate.LowestRate.as_view()),
]
