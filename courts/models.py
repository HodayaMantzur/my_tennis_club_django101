<<<<<<< HEAD
from django.db import models

from datetime import datetime
from django.db import models

class Court(models.Model):
  number = models.PositiveIntegerField(unique=True)
  is_occupied = models.BooleanField(default=False)
  time_of_occupation = models.DateTimeField(null=True)
  updated = models.DateTimeField(auto_now=True, null=True)
  created = models.DateTimeField(auto_now_add=True, null=True)

  def save(self, *args, **kwargs):
    if self.is_occupied:  # Update the time only if the court is occupied
        self.time_of_occupation = datetime.now()
    else:
        self.time_of_occupation = None  # Optionally reset the time when the court is not occupied
=======
from django.db import models

from datetime import datetime
from django.db import models

class Court(models.Model):
  number = models.PositiveIntegerField(unique=True)
  is_occupied = models.BooleanField(default=False)
  time_of_occupation = models.DateTimeField(null=True)
  updated = models.DateTimeField(auto_now=True, null=True)
  created = models.DateTimeField(auto_now_add=True, null=True)

  def save(self, *args, **kwargs):
    if self.is_occupied:  # Update the time only if the court is occupied
        self.time_of_occupation = datetime.now()
    else:
        self.time_of_occupation = None  # Optionally reset the time when the court is not occupied
>>>>>>> 6a028d562591f51c2fd9f4d8900b788561431771
    super().save(*args, **kwargs)