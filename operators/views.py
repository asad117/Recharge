from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny


class ServiceProviderViewSet(ModelViewSet):
    serializer_class = ServiceProviderSerializer
    queryset = ServiceProvider.objects.all()
    permission_classes = (AllowAny,)

class ZoneViewSet(ModelViewSet):
    serializer_class = ZoneSerializer
    queryset = Zone.objects.all()
    permission_classes = (AllowAny,)

class PlansViewSet(ModelViewSet):
    serializer_class = PlansSerializer
    queryset = Plans.objects.all()
    permission_classes = (AllowAny,)

class RechargeViewSet(ModelViewSet):
    serializer_class = RechargeSerializer
    queryset = Recharge.objects.all()
    permission_classes = (AllowAny,)





# class ResourceViewSet(ModelViewSet):
#     serializer_class = ResourceSerializer
#     queryset = Resource.objects.all()
#     permission_classes = (AllowAny,)

#     def create(self, request, *args, **kwargs):
#         data = request.data.copy()
#         data['company'] = request.user.company
#         pr_data = pre_processed_data(data)
#         pr_data['company'] = request.user.company.id
#         serializer = self.get_serializer(data=pr_data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=201, headers=headers)


