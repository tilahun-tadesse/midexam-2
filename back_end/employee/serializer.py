
from rest_framework import serializers
from .models import Employee_information


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_information
        fields = '__all__'
