from django.urls import path

from api import views

urlpatterns = [
    path("room_rates", views.RoomRateList.as_view()),
    path("room_rates/<int:room_id>", views.RoomRateDetail.as_view()),
]