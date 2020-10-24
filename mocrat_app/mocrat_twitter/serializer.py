from rest_framework import serializers

from mocrat_user.models import User
from allauth.socialaccount.models import SocialLogin, SocialToken, SocialApp, SocialAccount

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}