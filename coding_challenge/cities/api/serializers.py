from math import atan2, cos, radians, sin, sqrt

from rest_framework import serializers

from coding_challenge.cities.models import City
from coding_challenge.cities.utils import (
    cal_dis,
    get_score_with_lat_and_long,
    get_score_without_lat_and_long,
)


class CitySerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField(method_name='get_scores')

    class Meta:
        model = City
        fields = ['name', 'symbol', 'country', 'latitude', 'longitude', 'population', 'timeZone', "score"]

    def get_scores(self, obj):
        """
        Make the score number with respect to the nearest distances
        As the nearest has the highest score and as the distance is bigger
        the score is smaller
        """
        request = self.context.get("request")
        searched_name = request.GET.get("q", None)
        searched_lat = float(request.GET.get("latitude", 0))
        searched_long = float(request.GET.get("longitude", 0))

        current_object_name = obj.name
        current_object_lat = float(obj.latitude)
        current_object_long = float(obj.longitude)
        distance = cal_dis(
            current_object_lat, current_object_long,
            searched_lat, searched_long
        )
        
        # Make it default to 2 if no search done
        score = 2

        if searched_lat and searched_long:
            score = get_score_with_lat_and_long(distance)
        elif searched_name:
            score = get_score_without_lat_and_long(distance)
            if searched_lat == current_object_lat or searched_long == current_object_long:
                if score + 0.5 <= 1:
                    score += 0.4
        
        return score
