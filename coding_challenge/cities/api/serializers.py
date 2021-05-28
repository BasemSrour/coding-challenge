from math import atan2, cos, radians, sin, sqrt

from rest_framework import serializers

from coding_challenge.cities.models import City
from coding_challenge.cities.utils import calculate_distance2, get_score


class CitySuggestionsSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField(method_name='get_score')

    class Meta:
        model = City
        fields = ['name', 'symbol', 'country', 'latitude', 'longitude', 'population', "score"]

    def get_score(self, obj):
        """
        Make the score number with respect to the nearest distances
        As the nearest has the highest score and as the distance is bigger
        the score is smaller
        """
        # Get the needed to use variables and make sure they are float by casting them
        request = self.context.get("request")
        searched_lat = float(request.GET.get("latitude", 0))
        searched_long = float(request.GET.get("longitude", 0))
        current_object_lat = float(obj.latitude)
        current_object_long = float(obj.longitude)
        distance = calculate_distance2(
            (current_object_lat, current_object_long),
            (searched_lat, searched_long)
        )
        
        # Make it default to 2 if no search done
        # or if no q or lat or long is provided
        score = 2
        score = get_score(
            distance, searched_lat, current_object_lat,
            searched_long, current_object_long
        )
        
        return score
