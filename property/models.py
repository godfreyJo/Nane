from django.db import models
from django.conf import settings
from django.utils import timezone


class Customer_reg(models.Model):
    customer_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customer_Fname = models.CharField(max_length=200)
    customer_address = models.CharField(max_length=200)
    customer_county = models.CharField(max_length=200)
    customer_mobileNo = models.BigIntegerField()
    customer_email = models.CharField(max_length=20)

    def registered(self):
        self.registered_date = timezone.now()
        self.save()

    def __str__(self):
        return self.customer_Fname



