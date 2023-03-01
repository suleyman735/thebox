from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ReputationSeralizers
from .models import Reputation

# Create your views here.
class ReputationsViewSet(viewsets.ModelViewSet):
    serializer_class = ReputationSeralizers
    queryset = Reputation.objects.filter(available=True)