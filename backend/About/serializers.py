from rest_framework import serializers
from .models import AboutHeader,AboutExprience,AboutFront,PostImage,ProfesionalSection

class AboutHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutHeader
        fields = '__all__'
        
class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        # fields = '__all__'
        fields = ['image','title']

class ProfesionalSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfesionalSection
        fields = ['header','smallDescription','icon']
class AboutExprienceSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True)
    ProfesionalSection=ProfesionalSectionSerializer(many = True)
    class Meta:
        model = AboutExprience
        #fields = '__all__'
        fields = ['id','name','description','video','images','ProfesionalSection',]  
        
        

class AboutFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutFront
        fields = '__all__'