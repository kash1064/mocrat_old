import logging
import requests

from utils.mocrat_requests_classes import TwitterRequests

from mocrat_config.environ_config import env
from mocrat_config.post_texts import *

logger = logging.getLogger(__name__)

def call_twitter_post(twitter_user, text):
    '''
    python3 -c "from utils import mocrat_requests_utils; mocrat_requests_utils.call_twitter_post('chiba_moku2', 'test')"
    '''
    logger.info("Called mocrat_requests_utils call_twitter_post")
    print("call_twitter_post")

    twitter_requests = TwitterRequests(twitter_user)
    results = twitter_requests.twitter_post(text)
    print(results.status_code)
    return results


def call_get_tweet(twitter_user, query, count=10):
    '''
    python3 -c "from utils import mocrat_requests_utils; mocrat_requests_utils.call_get_tweet('chiba_moku2', 'python', 10)"
    '''
    logger.info("Called mocrat_requests_utils call_get_tweet")
    print("call_get_tweet")

    twitter_requests = TwitterRequests(twitter_user)
    results = twitter_requests.get_tweet(query, count)
    """
    result format
    [{'id': 1312276091659317248, 'text': 'this is text'},]
    """
    return results


def call_auto_fav_by_query(twitter_user, query, count=10):
    '''
    python3 -c "from utils import mocrat_requests_utils; mocrat_requests_utils.call_auto_fav_by_query('chiba_moku2', 'python', 10)"
    '''
    logger.info("Called mocrat_requests_utils call_auto_fav")
    print("call_auto_fav")

    tweets_arr = call_get_tweet(twitter_user, query, count)

    twitter_requests = TwitterRequests(twitter_user)
    tweet_ids = []
    for tweet in tweets_arr:
        if tweet["text"][0] == "@":
            continue
        tweet_ids.append(tweet["id"])
    
    results = twitter_requests.twiter_fav(tweet_ids)
    return results
        

    return results

if __name__ == "__main__":
    pass
