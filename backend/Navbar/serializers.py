from rest_framework import serializers
from .models import NavbarLogo,NavbarMenu

class NavbarLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavbarLogo
        fields = '__all__'
        
class NavbarMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavbarMenu
        fields = '__all__'