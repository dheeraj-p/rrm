from django.urls import include, path
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Room Rate Management API",
        default_version="v1",
        description="APIs for creating, overridding and discounting room rates",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

swagger_ui = schema_view.with_ui("swagger", cache_timeout=0)
swagger_formatter = schema_view.without_ui(cache_timeout=0)

urlpatterns = [
    path("swagger<format>/", swagger_formatter, name="schema-json"),
    path("swagger/", swagger_ui, name="schema-swagger-ui"),
    path("api/", include("api.urls")),
]
