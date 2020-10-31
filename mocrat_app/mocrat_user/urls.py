from django.urls import path
from . import views
from rest_framework import routers
from .views import UserViewSet, ChibaMokuUserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'chibamoku-user', ChibaMokuUserViewSet)
