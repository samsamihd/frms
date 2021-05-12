from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from frms.core.models import Layer, Feature, FloodPlain


@admin.register(Layer)
class LayerAdmin(admin.ModelAdmin):
    readonly_fields = ['code']


@admin.register(Feature)
class FeatureAdmin(LeafletGeoAdmin):
    default_zoom = 1
    readonly_fields = ['code']


@admin.register(FloodPlain)
class FloodPlainAdmin(LeafletGeoAdmin):
    default_zoom = 1
