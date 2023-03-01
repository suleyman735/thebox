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
    # images = models.FileField(upload_to = 'images/')
    description = models.TextField(max_length=280,null=True)
    video = models.FileField(upload_to='videos_uploaded',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

    def __str__(self):
      return self.name
    
class PostImage(models.Model):    
    post = models.ForeignKey(AboutExprience, default=None, related_name='images', on_delete=models.CASCADE)
    title = models.CharField(max_length=15,null=True,)
    image = models.FileField(upload_to = 'images/', )

    
    # def __file__(self):
    #     return '%d: %s' % (self.image, self.title)

    # class Meta:
        # unique_together = ['title', 'image','video']

 
    # def __str__(self):
    #     return self.title
    




# class Photo(models.Model):
#     # lesson = models.ForeignKey(AboutExprience, on_delete=models.CASCADE, related_name='photos')
#     photo = models.ImageField(upload_to="thebox/%Y/%m/%d/")

#     # resizing the image, you can change parameters like size and quality.
#     def save(self, *args, **kwargs):
#        super(Photo, self).save(*args, **kwargs)
#       #  img = Image.open(self.photo.path)
#       #  if img.height > 1125 or img.width > 1125:
#       #      img.thumbnail((1125,1125))
#       #  img.save(self.photo.path,quality=70,optimize=True)
       
#     def __str__(self):
#       return self.photo
      

    


    
