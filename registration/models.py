from django.db import models

# Create your models here.
class User(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=35)
    username = models.CharField(max_length=15)