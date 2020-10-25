import logging
import os
import requests

from rest_framework import authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from mocrat_user.models import User
from mocrat_config.environ_config import env

logger = logging.getLogger(__name__)

class PostText(APIView):
    def post(self, request):
        logger.info("Called mocrat_discord PostText")

        webhook_url = request.data["discord_webhook_url"]
        payload = {
            "content": request.data["text"]
        }
        requests.post(webhook_url, json=payload)
        return Response(status=200)
