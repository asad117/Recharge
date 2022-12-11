from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers
from .models import * 
from django.db import transaction
from operators.models import Recharge



class PaymentSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Payment

    def create(self, validated_data):

       with transaction.atomic():
           instance = Payment.objects.create(**validated_data)
           instance.save()
           br_instance = Recharge(mobile_number=self.initial_data['mobile_number'], service_provider=self.initial_data['provider'], plan=self.initial_data['plan'], type=self.initial_data['type'], payment=instance)
           br_instance.save()
       return instance