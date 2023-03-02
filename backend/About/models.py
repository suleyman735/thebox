from django.db import models
from django.core.validators import FileExtensionValidator
from PIL import Image
# Create your models here.

class AboutFront(models.Model):
    name = models.CharField(max_length=15,null=True,)
    slug = models.SlugField(max_length=50,unique=True,null=True)
    link = models.CharField(max_length=128,db_index=True,unique=True,blank=False,null=True)
    image = models.ImageField(upload_to="thebox/%Y/%m/%d/")
    available = models.BooleanField(default=True,null=True)
    def __str__(self):
      return self.name
  
class AboutHeader(models.Model):

    name = models.CharField(max_length=15,null=True,)

    description = models.TextField(max_length=280,null=True)
    # link = models.CharField(max_length=128,db_index=True,unique=True,blank=False,null=True)
    # image = models.ImageField(upload_to="thebox/%Y/%m/%d/")
    # available = models.BooleanField(default=True,null=True)
    # available1 = models.BooleanField(default=True,null=True)
    
    
    def __str__(self):
      return self.name
    

class AboutExprience(models.Model):
    name = models.CharField(max_length=15,null=True,)
    
    description = models.TextField(max_length=280,null=True)
    video = models.FileField(upload_to='videos_uploaded',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

    

    def __str__(self):
      return self.name
    
class PostImage(models.Model):    
    post = models.ForeignKey(AboutExprience, default=None, related_name='images', on_delete=models.CASCADE)
    title = models.CharField(max_length=15,null=True,)
    image = models.FileField(upload_to = 'images/', )
    
class ProfesionalSection(models.Model):
      header = models.TextField(max_length=280,null=True)
      smallDescription = models.TextField(max_length=280,null=True)
      icon = models.FileField(upload_to = 'images/', )
      post = models.ForeignKey(AboutExprience, default=None, related_name='ProfesionalSection', on_delete=models.CASCADE)

    
    
      

    


    
