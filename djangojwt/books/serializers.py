from rest_framework import serializers
from .models import books
import re

class BookSerializer(serializers.ModelSerializer):
    # Meta class is used to configure the metadata for serializer
    # It tells the serializer which model to use and which fileds from that model should be included.
    # Meta class inside a serializer helps configure how the serializer interacts with model, 
    # what fileds are exposed and how they are treated during serialization and deserialization
    class Meta:
        model=books
        fields= '__all__'

    def validate(self, data):
        pattern = r'^[0-9]+$'
        if not re.fullmatch(pattern, data['isbn']):
            raise serializers.ValidationError({'error': 'isbn must be numeric'})
        return data

