import requests
from django.core.management.base import BaseCommand
from places.models import Restaurant

class Command(BaseCommand):
    def handle(self, *args, **options): 
        url = "https://api.yelp.com/v3/businesses/search"
        API_KEY = "uNuYeA2IHXI3jBBE2tjiW3hOo8fkuxa2b3he7CclM2t1UJBZEuF8oRzLsRDdoGtiPCa0up7RBnRWrhNyFcmkkGnyt3F6QZbB4fZm7bH1qInply7j4NQ8fucf0O_hZXYx"
        headers = {'Authorization': f"Bearer {API_KEY}"}
        params = {"term": "restaurants", 'location': "Charlotte", 'limit': 50}
        response = requests.get(url, params=params, headers=headers)
        # print("This is the response: ", response)
        data = response.json()

        for i in data['businesses']:
            try:
                name = i['name']
            except:
                name = 'No name'
            try:
                address1 = i['location']['address1']
            except:
                address1 = ""
            try:
                address2 = i['location']['address2']
            except:
                address2 = ""
            try:
                address3 = i['location']['address3']
            except:
                address3 = ""
            try:
                address_city = i['location']['city']
                address_state = i['location']['state']
                address_zipcode = i['location']['zip_code']
            except:
                address_city = ""
                address_state = ""
                address_zipcode = ""
            try:
                tel_number = i['phone'][2:]
            except:
                tel_number = ""
            try: 
                rating = float(i['rating'])
            except:
                rating = 0.0
            try:
                price_point = len(i['price'])
            except:
                price_point = 0
            try:
                image_url = i['image_url']
            except:
                image_url = ""
            print(f"{name}, {address1}, {address2}, {address3}, {address_city}, {address_state}, {address_zipcode}, {tel_number} {rating}, {price_point}")
            res, created = Restaurant.objects.get_or_create(
                    name = name,
                    rating = rating,
                    price_point = price_point,
                    address1 = address1,
                    address2 = address2,
                    address3 = address3,
                    address_city = address_city,
                    address_state = address_state,
                    address_zipcode = address_zipcode,
                    tel_number = tel_number,
                    image_url = image_url
            )
            print(res, created)