import logging
import tweepy

from mocrat_config.environ_config import env
from mocrat_config.celery import app

logger = logging.getLogger(__name__)

#https://kurozumi.github.io/tweepy/api.html

# 認証
def get_auth_api(access_token, access_token_secret):
    twitter_api_key = env("TWITTER_API_KEY")
    twitter_api_secret = env("TWITTER_API_SECRET")

    auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)

    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api

# Twitter情報取得
def get_profile(api):
    return api.me()

# Tweet取得
# 試行当たりの最大数は20
def get_timeline_home(api):
    timeline_posts = api.home_timeline()
   
    return timeline_posts

#TODO:ちゃんとつくる
def get_user_tweets(api, user_id):
    user_tweets = api.user_timeline(user_id=user_id)
    for t in user_tweets:
        print(t)
    
    return user_tweets


# Tweet投稿
def post_twitter(api, text):
    api.update_status(text)


# いいね
def create_fav(api, tweet_id):
    logger.info("create_fav tweet id: " + str(tweet_id))
    api.create_favorite(tweet_id)

# 検索
def search_query_strings(api, query, count):
    return api.search(q=query, count=count)
    

if __name__ == "__main__":
    pass
