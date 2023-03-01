from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import NavbarLogoSerializer,NavbarMenuSerializer
from .models import NavbarLogo,NavbarMenu

# Create your views here.
class NavbarLogoViewSet(viewsets.ModelViewSet):
    serializer_class = NavbarLogoSerializer
    queryset = NavbarLogo.objects.all()
    
    
class NavbarMenuViewSet(viewsets.ModelViewSet):
    serializer_class = NavbarMenuSerializer
    queryset = NavbarMenu.objects.all()