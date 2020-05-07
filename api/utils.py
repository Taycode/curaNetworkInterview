import requests
from django.conf import settings

hotel_category_id = "500-5000-0053"
base_url = settings.BASE_URL
uri = '/discover/here'
url = base_url + uri


def get_hotels(latitude, longitude):
    lat_and_long = f'{latitude},{longitude}'
    params = {
        "at": lat_and_long,
        "apikey": settings.API_KEY,
        "cat": hotel_category_id
    }

    response = requests.get(url, params=params)
    return response.json()
