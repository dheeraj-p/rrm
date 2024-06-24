from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from api import models


room_id_param = openapi.Parameter(
    "room_id",
    openapi.IN_QUERY,
    description="room rate id for which lowest rate has to be found",
    type=openapi.TYPE_INTEGER,
    required=True,
)
from_date_param = openapi.Parameter(
    "from",
    openapi.IN_QUERY,
    description="Filter rates from date (in YYYY-MM-DD)",
    type=openapi.TYPE_STRING,
    required=True,
)
to_data_param = openapi.Parameter(
    "to",
    openapi.IN_QUERY,
    description="Filter rates to date (in YYYY-MM-DD)",
    type=openapi.TYPE_STRING,
    required=True,
)


class LowestRate(APIView):
    def apply_highest_discount(self, rate, discounts):
        highest_discount = 0

        for discount in discounts:
            discount_value = discount.discount_value
            if discount.discount_type == "percentage":
                discount_value = rate * discount_value / 100

            highest_discount = min(highest_discount, discount_value)

        return rate - highest_discount

    @swagger_auto_schema(
        manual_parameters=[room_id_param, from_date_param, to_data_param],
        responses={
            200: openapi.Response(
                "Lowest room rates available in the range of dates",
                openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "lowest_rate": {"type": openapi.TYPE_NUMBER},
                        "on_date": {
                            "type": openapi.TYPE_STRING,
                            "format": "Date(YYYY-MM-DD)",
                        },
                        "all_discounted_rates": {
                            "type": openapi.TYPE_ARRAY,
                        },
                    },
                ),
            )
        },
    )
    def get(self, request):
        room_id = request.GET.get("room_id", None)
        if room_id == None:
            return Response({"error": "'room_id' query param is required"}, status=400)

        from_date = request.GET.get("from", None)
        if from_date == None:
            return Response({"error": "'from' query param is required"}, status=400)

        to_date = request.GET.get("to", None)
        if to_date == None:
            return Response({"error": "'to' query param is required"}, status=400)

        room_rate = get_object_or_404(models.RoomRate, pk=room_id)
        overridden_rates = room_rate.overriddenroomrate_set.filter(
            stay_date__range=[from_date, to_date]
        )
        discounts = room_rate.discounts.all()

        all_discounted_rates = []
        lowest_rate = self.apply_highest_discount(room_rate.default_rate, discounts)
        on_date = "ALL_DAYS"

        all_discounted_rates.append({"lowest_rate": lowest_rate, "on_date": on_date})

        for o_rate in overridden_rates:
            discounted_rate = self.apply_highest_discount(
                o_rate.overridden_rate, discounts
            )
            if discounted_rate < lowest_rate:
                lowest_rate = discounted_rate
                on_date = o_rate.stay_date
                all_discounted_rates.append(
                    {"lowest_rate": lowest_rate, "on_date": on_date}
                )

        response = {
            "lowest_rate": lowest_rate,
            "on_date": on_date,
            "all_discounted_rates": all_discounted_rates,
        }

        return Response(response)
