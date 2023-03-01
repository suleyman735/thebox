from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import SliderSerializer
from .models import Slider

# Create your views here.
class SliderViewSet(viewsets.ModelViewSet):
    serializer_class = SliderSerializer
    queryset = Slider.objects.filter(available=True)