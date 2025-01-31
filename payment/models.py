from django.db import models

from common.models import User

# Create your models here.
class ProviderType(models.TextChoices):
    BANK = 'BANK', 'Bank'
    CARD = 'CARD', 'Card'
    MFS = 'MFS', 'Mobile Financial Service'

class PaymentProvider(models.Model):
    name = models.CharField(max_length=100)
    prvider_type = models.CharField(max_length=10, choices=ProviderType.choices)

    def __str__(self):
        return self.name

class Payment(models.Model):
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.ForeignKey(PaymentProvider, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.amount