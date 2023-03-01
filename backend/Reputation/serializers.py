from rest_framework import serializers
from .models import Reputation

class ReputationSeralizers(serializers.ModelSerializer):
        class Meta:
            model = Reputation
            fields = '__all__'