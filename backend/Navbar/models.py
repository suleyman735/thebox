from django.db import models

# Create your models here.
class NavbarLogo(models.Model):
    name = models.CharField(max_length=15)
    link = models.URLField(max_length=128,db_index=True,unique=True,blank=False)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/")
    available = models.BooleanField(default=True)
    
    def __str__(self):
      return self.name