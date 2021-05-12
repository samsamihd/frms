import json
import numpy as np
from rest_framework import response, views, viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from frms.core.models import Layer, Feature, FloodPlain
from frms.core.api.serializers import FeatureSerializer

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all().order_by('-created_at')
    serializer_class = FeatureSerializer


@api_view()
def affected(request, happened_at):
    floodplain = FloodPlain.objects.get(happened_at=happened_at)
    features = serializers.serialize('geojson', Feature.objects.filter(
        collection__intersects=floodplain.area))
    return response.Response({"message": "Get Affected Features Successfully!", "data": features})


@api_view()
def floodplain(request, happened_at):
    floodplain = FloodPlain.objects.filter(happened_at=happened_at)
    floodplain = serializers.serialize('geojson', floodplain, fields=["area"])
    return response.Response({"message": "Get Floodplain Successfully!", "data": floodplain})

@api_view()
def events(request):
    events = FloodPlain.objects.values_list('happened_at', flat=True).distinct()
    return response.Response({"message": "Get Events Features Successfully!", "data": events})