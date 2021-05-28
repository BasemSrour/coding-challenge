from math import atan2, cos, radians, sin, sqrt

from django.db.models.functions import ATan2, Cos, Power, Radians, Sin, Sqrt


def calculate_distance1(point1, point2):
    """
    Giving two points using Haversine distance

    Calculate the distance with the api view class that is used for suggestions endpoint.
    and filter the view using Django's Database functions.

    Note: Used only with view to avoid CombinedExpression errors which is generated when using with serailizer

    Writing it out with Django's Database functions.
    In contrast to raw SQL,
    this also gives the advantage of being able to easily append/prepend other ORM filters.
    """

    # Assign the vlues to these called variables to reflect the function's usage
    current_lat = point1[0]
    current_long = point1[1]
    searched_lat = point2[0]
    searched_long = point2[1]

    dlat = Radians(current_lat - searched_lat)
    dlong = Radians(current_long - searched_long)

    a = (Power(Sin(dlat / 2), 2) + Cos(Radians(searched_lat))
        * Cos(Radians(current_lat)) * Power(Sin(dlong / 2), 2))

    c = 2 * ATan2(Sqrt(a), Sqrt(1 - a))
    d = 6371 * c
    return d

def calculate_distance2(point1, point2):
    """
    Giving two points using Haversine distance.

    Note: Calculate the distance with the serializer class that is used for suggestions endpoint
    and get the score from the distance calculated from get_score method
    which can't be done using the previous method avoding to some errors and complexties.
    """

    # Assign the vlues to these called variables to reflect the function's usage
    current_lat = point1[0]
    current_long = point1[1]
    searched_lat = point2[0]
    searched_long = point2[1]

    dlat = radians(searched_lat - current_lat)
    dlon = radians(searched_long - current_long)

    a = (sin(dlat / 2))**2 + cos(radians(current_lat)) * cos(radians(searched_lat)) * (sin(dlon / 2))**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c

    return distance

def get_score(
    distance, searched_lat=None, current_object_lat=None,
    searched_long=None, current_object_long=None
):
    """
    Given: distance, searched_lat, current_object_lat,
    searched_long, current_object_long
    Evaluate score due to the distance range
    And increase it if the provided searched lat or long is exact to the current object lat or long
    
    Make the score number with respect to the nearest distances
    As the nearest has the highest score and as the distance is bigger
    the score is smaller
    
    These the quite good distances that I found from searching and testing
    """
    # When there is no lat or long provied
    # The distnace becom so far so i try to decrease it
    # To be like as there are provided lat and long
    if not searched_lat or not searched_long:
        distance -= 10000

    # Evaluate score due to the distance range
    score = 0.0
    score_distance_ranges = {
        1.0: (0, 200),
        0.9: (200, 400),
        0.8: (400, 600),
        0.7: (600, 800),
        0.6: (800, 1000),
        0.5: (1000, 1200),
        0.4: (1200, 1400),
        0.3: (1400, 3000),
        0.2: (3000, 4000),
        0.1: (4000, 5000)
    }
    for score, distance_range in score_distance_ranges.items():
        if distance_range[0] < distance <= distance_range[1]:
            score=score
            break
    
    # If the searched lat or long is exact to the current object lat or long
    if searched_lat == current_object_lat or searched_long == current_object_long:
        if score + 0.4 <= 1:
            # increase the score if the decreasing value won't override 1
            score += 0.4
    
    return score
