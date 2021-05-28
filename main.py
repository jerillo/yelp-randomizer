from secret import CLIENT_ID, API_KEY
from collections import defaultdict
import requests
import random
import json

from flask import Flask, render_template, request, redirect

def meters_to_miles(meters):
        return meters / 1609

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('form.html')

@app.route('/get_random_business', methods=['POST'])
def handle_data():
    form = request.form.to_dict()
    print('Search form values: ', form)
    business = get_random_business(form)
    if business:
        # For Debugging
        display_business(business)

        business['location'] = ',\n'.join(x for x in business['location']['display_address'])
        business['categories'] = ', '.join(str(x['title']) for x in business['categories'])
        business['distance'] = '{:.2f} miles'.format(meters_to_miles(business['distance']))
        business['rating_img'] = 'regular_' + str(business['rating']).replace('.5', '_half').replace('.0', '') + '.png'

    return render_template('result.html', business=business, location=form['location'], term=form['term'])

def get_random_business(params):
    search_url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer {}'.format(API_KEY)}
    response = requests.get(search_url, headers=headers, params=params)
    try:
        business = random.choice(response.json()['businesses'])
        return defaultdict(str, business)
    except:
        return None

def display_business(business):
    """Displays relevant information associated with business.

    Args:
        business (dict): business object returned from Yelp API search request.
    """
    def table_print(title, item):
        print('{:15} {}'.format(title + ':', item if item else 'Unknown'))

    if type(business) is not defaultdict:
        return

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
    params = dict()
    params['location'] = input('Enter a location: ')
    params['term'] = input('What are you looking for? ')

    print()

    try:
        business = defaultdict(str, get_random_business(params))
        display_business(business)
    except IndexError:
        print('No results found.')
