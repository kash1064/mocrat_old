from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateFav, GetProfile, GetTimelineHome, GetUserTweets, SearchQueryTweets, PostText

urlpatterns = [
    path('twitter_create_fav_url/', CreateFav.as_view()),
    path('get_profile/', GetProfile.as_view()),
    path('get_timeline_home/', GetTimelineHome.as_view()),
    path('get_user_tweets/', GetUserTweets.as_view()),
    path('search_query_tweets/', SearchQueryTweets.as_view()),
    path('post_text/', PostText.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
