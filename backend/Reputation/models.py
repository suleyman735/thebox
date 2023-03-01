from django.db import models

# Create your models here.
class Reputation(models.Model):
    icon = models.ImageField(upload_to="thebox/%Y/%m/%d/")
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=60)
    available = models.BooleanField(default=True)
    
    def __str__(self):
      return self.name