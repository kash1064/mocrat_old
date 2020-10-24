import logging

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostText

logger = logging.getLogger(__name__)

urlpatterns = [
    path('post_text/', PostText.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
