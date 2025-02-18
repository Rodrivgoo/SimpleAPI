from rest_framework import serializers
from .models import JSONData

class JSONDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = JSONData
        fields = '__all__'