from csv import DictReader
from os import environ

environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
import django

django.setup()
from coding_challenge.cities.models import City


def populate():
    with open("cities_canada-usa.csv", "r") as file:
        reader = DictReader(file)
        for row in reader:
            name = row["name"].strip()
            symbol = row["admin1"].strip()
            country = row["country"].strip()
            latitude = row["lat"].strip()
            longitude = row["long"].strip()
            population = row["population"].strip()
            city = add_city(name, symbol, country, latitude, longitude, population)
    
    for city in City.objects.all():
        print(f"City {str(city)} added")

def add_city(name, symbol, country, latitude, longitude, population):
    city = City.objects.get_or_create(
        name=name,
        symbol=symbol,
        country=country,
        latitude=latitude,
        longitude=longitude,
        population=population
    )[0]
    city.save()
    return city


if __name__ == "__main__":
    print("Populating the data from the CSV file")
    populate()
