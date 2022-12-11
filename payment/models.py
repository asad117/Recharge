from django.db import models
import uuid

# Create your models here.

class Payment(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  PAYMENT_MODE = (
    ('UPI', 'UPI'),
    ('Card', 'Card'),
    ('Net Banking', 'Net Banking'),
    ('Wallet', 'Wallet'),
  )
  mode = models.CharField(max_length=50, choices=PAYMENT_MODE, default='UPI')
  tranisition_id = models.CharField(max_length=50)
  amount = models.DecimalField(max_digits=6, decimal_places=2)
  provider = models.ForeignKey(to="operators.ServiceProvider", on_delete=models.CASCADE)
  # payer = models.ForeignKey(to="operators.Recharge", on_delete=models.CASCADE, related_name="paymet")
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return f'{self.amount} {self.payer.mobile_number}'
