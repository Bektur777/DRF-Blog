from rest_framework import serializers
from .models import *


class PortalSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Portal
        fields = "__all__"

