from typing import Any, Sequence

from factory import Faker
from factory.django import DjangoModelFactory
from coding_challenge.cities.models import City


class CityFactory(DjangoModelFactory):

    name = Faker("name")
    latitude = Faker("latitude")
    longitude = Faker("longitude")
    population = Faker("population")


    class Meta:
        model = City
