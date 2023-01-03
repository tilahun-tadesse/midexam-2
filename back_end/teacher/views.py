from django.shortcuts import render
from rest_framework import generics
from .srializer import teacherSerializer
from .models import teacher_information
# Create your views here.


class teacher_list(generics.ListCreateAPIView):
    queryset = teacher_information.objects.all()
    serializer_class = teacherSerializer


class teacher_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = teacher_information.objects.all()
    serializer_class = teacherSerializer
