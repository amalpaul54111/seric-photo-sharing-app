from django.db import models

# Create your models here.

# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    gender = models.CharField(max_length=6)
    password = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.name