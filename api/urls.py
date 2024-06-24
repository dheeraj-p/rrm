from django.urls import path

from api import views

urlpatterns = [
    path("room_rates", views.RoomRateList.as_view()),
    path("room_rates/<int:room_id>", views.RoomRateDetail.as_view()),
    path("overridden_rates", views.OverriddenRoomRateList.as_view()),
    path("overridden_rates/<int:id>", views.OverriddenRoomRateDetail.as_view()),
]