from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import urlpatterns

urlpatterns = [
    path('teacher-list/', teacher_list.as_view()),
    path('teacher-delete/<int:pk>', teacher_update.as_view())
]
