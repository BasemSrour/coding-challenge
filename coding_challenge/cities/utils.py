from math import atan2, cos, radians, sin, sqrt

from django.db.models.functions import ATan2, Cos, Power, Radians, Sin, Sqrt


def cal_distance(current_lat, current_long, searched_lat, searched_long):
    dlat = Radians(current_lat - searched_lat)
    dlong = Radians(current_long - searched_long)

    a = (Power(Sin(dlat / 2), 2) + Cos(Radians(searched_lat))
        * Cos(Radians(current_lat)) * Power(Sin(dlong / 2), 2))

    c = 2 * ATan2(Sqrt(a), Sqrt(1 - a))
    d = 6371 * c
    return d

def cal_dis(current_lat, current_long, searched_lat, searched_long):
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
    These the quite good distances that I found from searching and testing
    """
    # When there is no lat or long provied
    # The distnace becom so far so i try to decrease it
    # To be like as there are provided lat and long
    if not searched_lat or not searched_long:
        distance -= 10000

    # Evaluate score due to the distance range
    score = 0.0
    if distance <= 200:
        score = 1.0
    elif 200 < distance <= 400:
        score = 0.9
    elif 400 < distance <= 600:
        score = 0.8
    elif 600 < distance <= 800:
        score = 0.7
    elif 800 < distance <= 1000:
        score = 0.6
    elif 1000 < distance <= 1200:
        score = 0.5
    elif 1200 < distance <= 1400:
        score = 0.4
    elif 1400 < distance <= 3000:
        score = 0.3
    elif 3000 < distance <= 4000:
        score = 0.2
    elif distance > 4000:
        score = 0.1
    
    # If the searched lat or long is exact to the current object lat or long
    if searched_lat == current_object_lat or searched_long == current_object_long:
        if score + 0.4 <= 1:
            # increase the score if the decreasing value won't override 1
            score += 0.4
    
    return score
