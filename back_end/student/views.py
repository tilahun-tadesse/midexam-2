from django.shortcuts import render
from rest_framework import generics
from .serializer import studentSerializer
from .models import Student_information
# Create your views here.


class student_list(generics.ListCreateAPIView):
    queryset = Student_information.objects.all()
    serializer_class = studentSerializer


class student_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student_information.objects.all()
    serializer_class = studentSerializer
