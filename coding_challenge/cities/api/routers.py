from django.urls import path

from .views import CitiesAutoComplete

urlpatterns = [
    path("suggestions/", view=CitiesAutoComplete.as_view(), name="cities-suggestions"),
]
