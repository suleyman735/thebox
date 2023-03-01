from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .serializers import AboutHeaderSerializer,AboutExprienceSerializer,AboutFrontSerializer
from .models import AboutHeader,AboutFront,AboutExprience,PostImage
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.
class AboutHeaderViewSet(viewsets.ModelViewSet):
    serializer_class = AboutHeaderSerializer
    queryset = AboutHeader.objects.all()
    
    
class AboutFrontViewSet(viewsets.ModelViewSet):
    serializer_class = AboutFrontSerializer
    queryset = AboutFront.objects.all()
    
class AboutExprienceViewSet(viewsets.ModelViewSet):
    serializer_class = AboutExprienceSerializer
    # renderer_classes = [JSONRenderer]
    queryset = AboutExprience.objects.all()
