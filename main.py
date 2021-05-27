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


def get_random_business(location, term):
    search_url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer {}'.format(API_KEY)}
    params = {
        'location': location,
        'term': term
    }
    response = requests.get(search_url, headers=headers, params=params)
    business = random.choice(response.json()['businesses'])
    return business


def display_business(business):
    """Displays relevant information associated with business.

    Args:
        business (dict): business object returned from Yelp API search request.
    """
    def table_print(title, item):
        print('{:15} {}'.format(title + ':', item))

    def meters_to_miles(meters):
        return meters / 1609

    table_print('Name', business['name'])
    table_print('Phone', business['phone'])
    table_print('Location',
                ', '.join(x for x in business['location']['display_address']))
    table_print('Distance', '{:.2f} miles'.format(meters_to_miles(business['distance'])))
    table_print('Price', business['price'])
    table_print('Rating', business['rating'])
    table_print('Review Count', business['review_count'])
    table_print('URL', business['url'])
    table_print('Categories',
                ', '.join(str(x['title']) for x in business['categories']))


if __name__ == '__main__':
    location = input('Enter a city: ')
    term = input('What are you looking for? ')
    business = get_random_business(location, term)
    display_business(business)
