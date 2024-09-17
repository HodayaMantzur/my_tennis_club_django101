<<<<<<< HEAD
from django.db import models

# Create your models here.

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
=======
from django.db import models

# Create your models here.

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
>>>>>>> 6a028d562591f51c2fd9f4d8900b788561431771
  joined_date = models.DateField(null=True)