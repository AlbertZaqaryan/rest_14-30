from django.shortcuts import render
from .serializers import PhoneSerializers
from .models import Phone
from rest_framework import viewsets
# Create your views here.

class PhoeViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializers

