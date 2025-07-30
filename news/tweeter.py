from django.conf import settings
import tweepy

BEARER_TOKEN = getattr(settings, "BEARER_TOKEN", None)
ACCESS_KEY = getattr(settings, "ACCESS_KEY", None)
ACCESS_SECRET = getattr(settings, "ACCESS_SECRET", None)
CONSUMER_KEY = getattr(settings, "CONSUMER_KEY", None)
CONSUMER_SECRET = getattr(settings, "CONSUMER_SECRET", None)


def send_new_tweet(text):
    # Syntax for Tweeter API 2.0
    newapi = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        access_token=ACCESS_KEY,
        access_token_secret=ACCESS_SECRET,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
    )

    new_tweet = newapi.create_tweet(text=text)
    print(new_tweet)