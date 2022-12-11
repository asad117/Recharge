from django.contrib import admin
from operators.models import *

# Register your models here.
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ('operator_name',)

class ZoneAdmin(admin.ModelAdmin):
    list_display = ('zone_name',)

class PlansAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'providers')


class RechargeAdmin(admin.ModelAdmin):
    list_display = ('mobile_number', 'plan')

admin.site.register(ServiceProvider, ServiceProviderAdmin)
admin.site.register(Plans,PlansAdmin)
admin.site.register(Zone,ZoneAdmin)
admin.site.register(Recharge,RechargeAdmin)





