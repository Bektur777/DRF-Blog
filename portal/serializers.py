from rest_framework import serializers
from .models import *


class PortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portal
        fields = "__all__"


# def encode():
#     model = PostModel("Hello", "world")
#     model_sr = PortalSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep="\n")
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Hello","content":"world"}')
#     data = JSONParser().parse(stream)
#     serializer = PortalSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
