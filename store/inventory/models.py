from django.db import models
from django.conf import settings
# Create your models here.


class Stock(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField()
    SellingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    PurchasePrice = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1234567)

