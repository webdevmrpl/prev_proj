from django.shortcuts import render
from rest_framework import viewsets
from .models import Data
from .serializers import DataSerializer


class DataView(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
