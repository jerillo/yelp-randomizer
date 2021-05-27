from secret import CLIENT_ID, API_KEY
from collections import defaultdict
import requests
import random
import json

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('form.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    form = request.form.to_dict()
    location = form['location']
    print('Search form values: ', form)
    res = get_random_business(form)
    display_business(res)
    return """
    <a href="{}" target="_blank">{}</a>
    <button onclick="location.href='/'" type="button">
         Randomize again</button>
    """.format(res['url'], res['name'])

def get_random_business(params):
    search_url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer {}'.format(API_KEY)}
    response = requests.get(search_url, headers=headers, params=params)
    try:
        business = random.choice(response.json()['businesses'])
    except:
        return { 'name': 'No results found.' }
    return defaultdict(str, business)


def display_business(business):
    """Displays relevant information associated with business.

    Args:
        business (dict): business object returned from Yelp API search request.
    """
    def table_print(title, item):
        print('{:15} {}'.format(title + ':', item if item else 'Unknown'))

    def meters_to_miles(meters):
        return meters / 1609

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
