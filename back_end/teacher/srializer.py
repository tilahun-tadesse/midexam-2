from rest_framework import serializers
from .models import teacher_information


class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher_information
        fields = '__all__'
