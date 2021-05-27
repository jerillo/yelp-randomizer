from secret import CLIENT_ID, API_KEY
import requests
import random
import json


def jprint(obj):
    """
        Create a formatted string of the Python JSON object
        Source: https://www.dataquest.io/blog/python-api-tutorial/
    """
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def get_random_restaurant(location):
    search_url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer {}'.format(API_KEY)}
    params = {
        'location': location
    }
    response = requests.get(search_url, headers=headers, params=params)
    restaurant = random.choice(response.json()['businesses'])
    return restaurant


def display_restaurant(restaurant):
    """Displays relevant information associated with restaurant.

    Args:
        restaurant (dict): Restaurant object returned from Yelp API search request.
    """
    def table_print(title, item):
        print('{:15} {}'.format(title + ':', item))

    def meters_to_miles(meters):
        return meters / 1609

    table_print('Name', restaurant['name'])
    table_print('Phone', restaurant['phone'])
    table_print('Location',
                ', '.join(x for x in restaurant['location']['display_address']))
    table_print('Distance', '{:.2f} miles'.format(meters_to_miles(restaurant['distance'])))
    table_print('Price', restaurant['price'])
    table_print('Rating', restaurant['rating'])
    table_print('Review Count', restaurant['review_count'])
    table_print('URL', restaurant['url'])
    table_print('Categories',
                ', '.join(str(x['title']) for x in restaurant['categories']))


if __name__ == '__main__':
    location = input('Enter a city: ')
    restaurant = get_random_restaurant(location)
    display_restaurant(restaurant)
