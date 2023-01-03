from django.shortcuts import render

from rest_framework import generics
from .serializer import employeeSerializer
from .models import Employee_information
# Create your views here.


class employee_list(generics.ListCreateAPIView):
    queryset = Employee_information.objects.all()
    serializer_class = employeeSerializer


class employee_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee_information.objects.all()
    serializer_class = employeeSerializer
