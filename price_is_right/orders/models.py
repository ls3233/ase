from __future__ import unicode_literals
from django.db import models
# from authentication.models import UserProfile

class ParentOrder(models.Model):
    # user = models.ForeignKey(UserProfile)
    quantity = models.IntegerField(blank=False, help_text="Total quantity of parent order")
    stock_type = models.CharField(blank=True, max_length=10)
    stock_name = models.CharField(blank=True, max_length=10)
    is_sell = models.BooleanField(blank=False, default=True)
    time_executed = models.DateTimeField(blank=False, auto_now_add=True)
    success = models.BooleanField(default=False)


class ChildOrder(models.Model):
    parent_order = models.ForeignKey(ParentOrder)
    quantity = models.IntegerField(blank=False)
    success = models.BooleanField(blank=False, default=False)
    price = models.IntegerField(blank=False)
    time_executed = models.DateTimeField(blank=False, auto_now_add=True)
