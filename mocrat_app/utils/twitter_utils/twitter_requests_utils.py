import logging
import os
import requests
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from mocrat_config.admin_utils import error_notify
from mocrat_config.environ_config import env
from mocrat_config.post_texts import *

logger = logging.getLogger(__name__)

base_url = env("BASE_URL")

class TwitterRequests(object):
    def __init__(self, twitter_user):
        self.twitter_user = twitter_user

        print("Called mocrat_requests_classes TwitterRequests")
        print("Twitter user is : " + self.twitter_user)

    #get info
    def get_tweet(self, query, count):
        twitter_search_query_url = env("TWITTER_SERCH_QUERY_API")
        twitter_payload = {
            "twitter_user": self.twitter_user,
            "query": query,
            "count": count
        }
        search_results = requests.get(base_url + twitter_search_query_url, params=twitter_payload)
        search_results = search_results.json()
        return search_results

    #actions
    def twitter_post(self, text):
        '''
        curl - X POST - H "Content-Type: application/json" - d '{ "text":"投稿" }' chiba-moku2.herokuapp.com/mocrat_twitter/api/v1/post_text/ -H "Authorization: JWT <TOKEN>"
        '''
        logger.info("Called mocrat_requests_classes TwitterRequests.twitter_post")
        twitter_post_url = env("TWITTER_POST_API")
        twitter_payload = {
            "twitter_user": self.twitter_user,
            "text": text,
        }
        results = requests.post(base_url + twitter_post_url, data=twitter_payload)
        return results
    

    def twiter_fav(self, tweet_ids):
        logger.info("Called mocrat_requests_classes TwitterRequests.twitter_post")
        twitter_create_fav_url = env("TWITTER_CREATE_FAV_API")
        twitter_payload = {
            "twitter_user": self.twitter_user,
            "tweet_ids": tweet_ids,
        }
        results = requests.post(base_url + twitter_create_fav_url, data=twitter_payload)
        return results

def call_twitter_post(twitter_user, text):
    logger.info("Called twitter_requests_utils call_twitter_post")

    twitter_requests = TwitterRequests(twitter_user)
    results = twitter_requests.twitter_post(text)

    return results


def call_get_tweet(twitter_user, query, count=10):
    logger.info("Called twitter_requests_utils call_get_tweet")

    twitter_requests = TwitterRequests(twitter_user)
    results = twitter_requests.get_tweet(query, count)
    """
    result format
    [{'id': 1312276091659317248, 'text': 'this is text'},]
    """
    return results


def call_auto_fav_by_query(twitter_user, query, count=10):
    logger.info("Called twitter_requests_utils call_auto_fav")

    tweets_arr = call_get_tweet(twitter_user, query, count)

    twitter_requests = TwitterRequests(twitter_user)
    tweet_ids = []
    for tweet in tweets_arr:
        if tweet["text"][0] == "@":
            continue
        tweet_ids.append(tweet["id"])
    
    results = twitter_requests.twiter_fav(tweet_ids)
    return results
        

if __name__ == "__main__":
    pass
