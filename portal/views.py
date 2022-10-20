from rest_framework import generics
from rest_framework.permissions import *

from .models import *
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import PortalSerializer


class PortalAPIList(generics.ListAPIView):
    queryset = Portal.objects.all()
    serializer_class = PortalSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PortalAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Portal.objects.all()
    serializer_class = PortalSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PortalAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Portal.objects.all()
    serializer_class = PortalSerializer
    permission_classes = (IsAdminOrReadOnly,)
