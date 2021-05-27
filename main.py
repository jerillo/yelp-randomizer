from secret import CLIENT_ID, API_KEY
import requests
import json


def jprint(obj):
    # create a formatted string of the Python JSON object
    # Source: https://www.dataquest.io/blog/python-api-tutorial/
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# Test simple API request to business search endpoint
url = 'https://api.yelp.com/v3/businesses/search'
response = requests.get(
    url, headers={'Authorization': 'Bearer {}'.format(API_KEY)}, params={
        'location': 'New York City',
        'limit': 1
    })

res = response.json()['businesses']

jprint(res)
