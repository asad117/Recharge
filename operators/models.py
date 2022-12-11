from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
import uuid




class ServiceProvider(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  operator_name = models.CharField(max_length=25)
  def __str__(self):
        return f'{self.operator_name}'


class Zone(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    zone_name = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.zone_name}'


class Plans(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=50)
  PLANS_CHOICES = (
    ('prepaid', 'Prepaid'),
    ('postpaid', 'Pospaid'),
  )
  type = models.CharField(max_length=50, choices=PLANS_CHOICES, default='prepaid')
  price = models.DecimalField(max_digits=6, decimal_places=2)
  validity = models.CharField(max_length=20)
  data = models.CharField(max_length=20)
  sms = models.CharField(max_length=20)
  other_benifits = models.CharField(max_length=200)
  zone = models.ForeignKey(to="operators.Zone", on_delete=models.CASCADE)
  providers = models.ForeignKey(to="operators.ServiceProvider", on_delete=models.CASCADE)
  def __str__(self):
        return f'{self.type} {self.name}'



def number_validate(value):
  if len(str(value)) <= 12 and len(str(value))>=10:
    return value
  else:
    raise ValidationError("Please Enter the Valid Mobile Number")
 
class Recharge(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  mobile_number = models.PositiveIntegerField(validators=[number_validate])
  service_provider = models.ForeignKey(to="operators.ServiceProvider", on_delete=models.CASCADE)
  plan = models.ForeignKey(to="operators.Plans", on_delete=models.CASCADE)
  PLANS_CHOICES = (
    ('prepaid', 'Prepaid'),
    ('postpaid', 'Pospaid'),
  )
  type = models.CharField(max_length=20, choices=PLANS_CHOICES, default='prepaid')
  date = models.DateTimeField(auto_now_add=True)
  payment = models.ForeignKey(to="payment.Payment", on_delete=models.SET_NULL, related_name="recharge", null=True, blank=True)
