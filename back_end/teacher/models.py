from django.db import models

# Create your models here.


class teacher_information(models.Model):

    firstName = models.CharField(max_length=40)
