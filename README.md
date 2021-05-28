# Yelp Randomizer

**Author: Jesnine Erillo**

This application randomly selects a business given a search query using the Yelp Fusion API. There are two ways to run this program: with a command-line interface or as a web app. The web app version is built with Flask.

## Inspiration

My friends and I always spend so much time just trying to decide on where to go, so this simplifies that thought process by making a decision for us! :)

## Running Locally 

1. Create a Yelp app to retrieve your API Key: [https://www.yelp.com/developers/v3/manage_app](https://www.yelp.com/developers/v3/manage_app)
2. Enter your private API Keys into `secret.py.example` and rename the file to `secret.py`
3. You can run with either a command-line interface or as a simple Flask web app:
    - **For CLI:** Run `python3 main.py`
    - **For Web app:** Run `export FLASK_APP=main` then `flask run`

## Preview

### Web app interface

![web-home](preview/web-home.png)
![web-search-result](preview/web-search-result.png)

### CLI

Here we can see that I entered "UC Berkeley" as my search location and specified that I was looking for "KBBQ". In the screenshot below, I ran the program twice with the same values so you can see that the output is randomized.

![preview](preview/berkeley-kbbq.png)
