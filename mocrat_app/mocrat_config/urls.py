from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from mocrat_user.urls import router as user_router


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('auth/', include('allauth.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^mocrat_main/api/v1/', include('mocrat_main.urls')),
    url(r'^mocrat_utils/api/v1/', include('mocrat_utils.urls')),
    url(r'^mocrat_discord/api/v1/', include('mocrat_discord.urls')),
    url(r'^mocrat_twitter/api/v1/', include('mocrat_twitter.urls')),
    url(r'^mocrat_user/api/v1/', include(user_router.urls)),
]
