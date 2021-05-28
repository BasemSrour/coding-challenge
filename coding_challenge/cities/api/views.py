from django.db.models import F
from rest_framework.generics import ListAPIView

from coding_challenge.cities.models import City
from coding_challenge.cities.utils import calculate_distance1

from .serializers import CitySuggestionsSerializer


class CitiesSuggestions(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySuggestionsSerializer

    def get_queryset(self):
        """
        Get the query of the first ten sorted due to the distance
        in ascending order

        Return only the first 10 results to minimize the resulted data and
        time of loading if they are so many or if no q provided
        """
        filters = {}
        searched_lat = float(self.request.GET.get("latitude", 0))
        searched_long = float(self.request.GET.get("longitude", 0))
        q = self.request.GET.get("q", None)
        
        if q:
            filters["name__icontains"] = q

        current_lat = F('latitude')
        current_long = F('longitude')
        d = calculate_distance1(
            (current_lat, current_long), 
            (searched_lat, searched_long)
        )

        return City.objects.annotate(distance=d).order_by('distance').filter(**filters)[:10]
