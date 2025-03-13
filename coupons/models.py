from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AnonymousUser

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    is_claimed = models.BooleanField(default=False)

    def __str__(self):
        return self.code

class CouponClaim(models.Model):
    ip_address = models.GenericIPAddressField()
    session_id = models.CharField(max_length=255, blank=True, null=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"Coupon {self.coupon.code} claimed by {self.ip_address}"
