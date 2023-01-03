from django.db import models

# Create your models here.


class Student_information(models.Model):
    firstName = models.CharField(max_length=40)
