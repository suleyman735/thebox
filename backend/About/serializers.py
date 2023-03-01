from rest_framework import serializers
from .models import AboutHeader,AboutExprience,AboutFront,PostImage

class AboutHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutHeader
        fields = '__all__'
        
class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        # fields = '__all__'
        fields = ['image','title']
        
class AboutExprienceSerializer(serializers.ModelSerializer):
    # title = serializers.RelatedField(source = )
    class Meta:
        model = AboutExprience
        #fields = '__all__'
        fields = ['id','name','description','video','images',]   
 
        
 
class AboutFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutFront
        fields = '__all__'