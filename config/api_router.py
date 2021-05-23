from django.conf import settings
from django.urls.conf import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from coding_challenge.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

patterns = [
    path("cities/", include("coding_challenge.cities.api.routers")),
]


app_name = "api"
urlpatterns = router.urls + patterns
