from rest_framework import serializers
from .models import User, ChibaMokuUser, ChibaMokuActivityLog


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}


class ChibaMokuUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChibaMokuUser
        # fields = [
        #     'discord_id',
        #     'display_name',
        #     'level',
        #     'total_exp',
        #     'created_at',
        #     'updated_at',
        # ]
        exclude = ['created_at']


class ChibaMokuActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChibaMokuActivityLog
        # fields = [
        #     'chibamoku_activity',
        #     'category',
        #     'level',
        #     'created_at',
        #     'updated_at',
        # ]
        exclude = ['created_at']