from django.db import models

# Create your models here.

class Slider(models.Model):
    image=models.ImageField(upload_to="thebox/%Y/%m/%d/",null=True)
    imgDesc=models.CharField(max_length=15,null=True)
    futPro=models.CharField(max_length=15,null=True)
    proName=models.CharField(max_length=15,null=True)
    available = models.BooleanField(default=True)
    
    def __str__(self):
      return self.proName