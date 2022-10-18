from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import PortalSerializer

# Create your views here.


class PortalModelViewSet(viewsets.ModelViewSet):
    queryset = Portal.objects.all()
    serializer_class = PortalSerializer


# class PortalAPIView(APIView):
#     def get(self, request):
#         p = Portal.objects.all()
#         return Response({'posts': PortalSerializer(p, many=True).data})
#
#     def post(self, request):
#         serializer = PortalSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"Error": "Method put not allowed"})
#
#         try:
#             instance = Portal.objects.get(pk=pk)
#         except:
#             return Response({"Error": "Object doesn't exist"})
#
#         serializer = PortalSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})

