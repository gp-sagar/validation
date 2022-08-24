from django.db import models

# Create your models here.
class User(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=35)
    username = models.CharField(max_length=15)

class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
    device_name = models.TextField(max_length=30)
    device_id = models.CharField(max_length=50)
    device_status = models.TextField(max_length=5)


