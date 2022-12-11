from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("service_provider", ServiceProviderViewSet, "service_provider"),
router.register("zone", ZoneViewSet, "zone"),
router.register("plans", PlansViewSet, "plans"),
router.register("recharge", RechargeViewSet, "recharge"),





urlpatterns = [] + router.urls
