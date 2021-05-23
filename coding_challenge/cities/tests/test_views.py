from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from coding_challenge.cities.models import City
from .factories import CityFactory
from coding_challenge.users.tests.factories import UserFactory


class TestCitiesAutoCompleteAPIViews(APITestCase):

    def setUp(self):
        self.user = UserFactory.create(name="Bassem")
        self.client = APIClient()
        token, _ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        cities = {
            "Oatfield": {"lat": "45.414180", "long": "-122.600070"},
            "West Side Highway": {"lat": "46.183990", "long": "-122.917150"},
            "Dixiana": {"lat": "33.740210", "long": "-86.649380"},
            "Bridgewater": {"lat": "41.990380", "long": "-70.975040"},
            "Makakilo": {"lat": "21.346940", "long": "-158.085830"},
            "London": {"lat": "37.128980", "long": "-84.083260"},
            "Amherst": {"lat": "42.375370", "long": "-72.519250"},
            "Cocoa West": {"lat": "28.359420", "long": "-80.771090"},
            "Pacific": {"lat": "38.482000", "long": "-90.741520"},
            "Hinton": {"lat": "53.400090", "long": "-117.585670"}
        }
        
        for city_name, city_data in cities.items():
            self.city = CityFactory.create(
                name=city_name,
                latitude=city_data["lat"],
                longitude=city_data["long"],
                population=0
            )

    def test_lowercase_complete_name_only(self):
        city_name = "London"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 1)
    
    def test_lowercase_complete_name_with_lat_and_long(self):
        city_name = "London"
        lat = "37.128980"
        long = "-84.083260"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}&latitude={lat}&longitude={long}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 1)

    def test_lowercase_beginning_truncated_name_only(self):
        city_name = "oatf"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 1)
    
    def test_lowercase_beginning_truncated_name_with_lat_only(self):
        city_name = "oatf"
        lat = "45.414180"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}&latitude={lat}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 1)

    def test_lowercase_middle_truncated_name_only(self):
        city_name = "st side hig"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 1)
    
    def test_lowercase_middle_truncated_name_with_long_only(self):
        city_name = "st side hig"
        long = "-122.917150"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}&longitude={long}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 1)

    def test_lowercase_ending_truncated_name_only(self):
        city_name = "iana"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 1)
    
    def test_lowercase_ending_truncated_name_with_latitude_and_longitude(self):
        city_name = "iana"
        lat = "33.740210"
        long = "-86.649380"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}&latitude={lat}&longitude={long}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 1)
    
    def test_uppercase_comlete_name_only(self):
        city_name = "PACIFIC"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 1)

    def test_uppercase_comlete_name_with_lat_only(self):
        city_name = "PACIFIC"
        lat = "38.482000"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}&latitude={lat}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 1)

    def test_uppercase_beginning_truncated_name_only(self):
        city_name = "AMHE"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 1)
    
    def test_uppercase_beginning_truncated_name_with_long_only(self):
        city_name = "AMHE"
        long = "-72.519250"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}&longitude={long}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 1)

    def test_uppercase_middle_truncated_name_only(self):
        city_name = "INT"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 1)

    def test_uppercase_middle_truncated_name_with_lat_and_long(self):
        city_name = "INT"
        lat = "53.400090"
        long = "-117.585670"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}&latitude={lat}&longitude={long}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 1)

    def test_uppercase_ending_truncated_name_only(self):
        city_name = "ALY"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 0)
    
    def test_uppercase_ending_truncated_name_with_lat_only(self):
        city_name = "ALY"
        lat = "42.375370"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}&latitude={lat}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 0)
    
    def test_uppercase_ending_truncated_name_with_long_only(self):
        city_name = "ALY"
        long = "-70.975040"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}&longitude={long}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 0)
    
    def test_uppercase_ending_truncated_name_with_lat_and_long(self):
        city_name = "ALY"
        lat = "21.346940"
        long = "-70.975040"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}&latitude={lat}&longitude={long}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 0)

    def test_capitalize_completed_name_only(self):
        city_name = "Bridgewater"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 1)
    
    def test_capitalize_completed_name_with_long_only(self):
        city_name = "Bridgewater"
        long = "-70.975040"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}&longitude={long}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 1)

    def test_capitalize_beginning_truncated_name_only(self):
        city_name = "Maka"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 1)

    def test_capitalize_beginning_truncated_name_with_lat_and_long(self):
        city_name = "Maka"
        lat = "21.346940" 
        long = "-158.085830"
        response = self.client.get(
            f'/api/cities/suggestions/?q={city_name}&latitude={lat}&longitude={long}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(len(response), 1)
