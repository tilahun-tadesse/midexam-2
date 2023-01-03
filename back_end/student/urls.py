from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import urlpatterns

urlpatterns = [
    path('student-list/', student_list.as_view()),
    path('student-delete/<int:pk>', student_update.as_view())
]
