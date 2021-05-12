from rest_framework import serializers
from frms.core.models import Layer, Feature, FloodPlain


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'
