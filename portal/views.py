from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import PortalSerializer

# Create your views here.


class PortalAPIView(generics.ListAPIView):
    queryset = Portal.objects.all()
    serializer_class = PortalSerializer
