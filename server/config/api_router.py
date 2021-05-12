from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from frms.users.api.views import UserViewSet
from frms.core.api.views import FeatureViewSet, affected, floodplain, events

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path('floodplains/detail/<happened_at>/', floodplain, name='floodplains'),
    path('floodplains/events/', events, name='floodplains_events'),
    path('features/<happened_at>/', affected, name='affected_features'),
]
