from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers
from .models import * 
from django.db import transaction
from payment.models import Payment



class ServiceProviderSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ServiceProvider

class PlansSerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Plans

class ZoneSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Zone

class RechargeSerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Recharge


