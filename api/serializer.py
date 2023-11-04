from rest_framework import serializers
from .models import *
class Bus(serializers.Modelserializer):
    class Meta:
        model = Bus