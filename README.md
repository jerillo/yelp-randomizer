# Yelp Randomizer

**Author: Jesnine Erillo**

This application randomly selects a business given a search query.

In the future, I plan on creating a simple UI and hosting this somewhere so I can share it with people and use it on the go.

## Inspiration

My friends and I always spend so much time just trying to decide on where to go, so this simplifies that thought process by choosing for us! :)

## Running Locally

1. Create a Yelp app to retrieve your API Key: [https://www.yelp.com/developers/v3/manage_app](https://www.yelp.com/developers/v3/manage_app)
2. Enter your private API Keys into `secret.py.example` and rename the file to `secret.py`
3. Run `python3 main.py`

## Preview

Here we can see that I entered "UC Berkeley" as my search location and specified that I was looking for "KBBQ". In the screenshot below, I ran the program twice with the same values so you can see that the output is randomized.

![preview](preview/berkeley-kbbq.png)
