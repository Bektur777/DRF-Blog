from rest_framework import serializers
from .models import *


class PortalSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Portal
        fields = ('title', 'cat_id')
