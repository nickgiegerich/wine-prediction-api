from rest_framework import serializers
from rest_framework.fields import ChoiceField
from .models import Wine

class WineSerializer(serializers.ModelSerializer):
    # model_to_run = ChoiceField(choices=Wine.MODEL_CHOICES, default='RF')
    class Meta:
        model = Wine
        fields = '__all__'