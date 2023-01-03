from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import urlpatterns

urlpatterns = [
    path('employee-list/', employee_list.as_view()),
    path('employee-delete/<int:pk>', employee_update.as_view())
]
