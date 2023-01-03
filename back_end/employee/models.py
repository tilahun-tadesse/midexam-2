from django.db import models

# Create your models here.


class Employee_information(models.Model):

    firstName = models.CharField(max_length=40)
