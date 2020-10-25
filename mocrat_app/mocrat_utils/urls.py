from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AsakatsuClosing, AsakatsuSchedule


# curl -X GET localhost:8000/mocrat_main/api/v1/asakatsu_closing/
urlpatterns = [
    path('asakatsu_closing/', AsakatsuClosing.as_view()),
    path('asakatsu_scheduler/', AsakatsuSchedule.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)