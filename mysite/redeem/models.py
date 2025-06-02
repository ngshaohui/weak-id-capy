from django.db import models


class Coupon(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=40)
    status = models.BooleanField()
    updated_at = models.DateTimeField(auto_now_add=True)


class ManualProtection(models.Model):
    id = models.IntegerField(primary_key=True)
    attempts = models.IntegerField(default=0)
