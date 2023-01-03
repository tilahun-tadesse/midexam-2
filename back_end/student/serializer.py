from rest_framework import serializers
from .models import Student_information


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_information
        fields = '__all__'
