from rest_framework import serializers
from .models import Basic


class BasicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Basic
        fields = ('temp', 'moist')
