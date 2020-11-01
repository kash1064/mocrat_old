from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import User, ChibaMokuUser, ChibaMokuActivityLog
from .serializer import UserSerializer, ChibaMokuUserSerializer, ChibaMokuActivityLogSerializer

from mocrat_config.admin_utils import error_notify

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # UserNameで1件取得
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, username=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    # TODO:Destroy管理者以外でも消せるのは問題では
    def destroy(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, username=pk)
        self.perform_destroy(user)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class ChibaMokuUserViewSet(viewsets.ModelViewSet):
    queryset = ChibaMokuUser.objects.all()
    serializer_class = ChibaMokuUserSerializer


class ChibaMokuActivityLogViewSet(viewsets.ModelViewSet):
    queryset = ChibaMokuActivityLog.objects.all()
    serializer_class = ChibaMokuActivityLogSerializer