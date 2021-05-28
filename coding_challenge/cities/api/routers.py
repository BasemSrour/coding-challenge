from django.urls import path

from .views import CitiesSuggestions

urlpatterns = [
    path("suggestions/", view=CitiesSuggestions.as_view(), name="cities-suggestions"),
]
