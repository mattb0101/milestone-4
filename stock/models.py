from django.db import models

from products.models import Product


class Stock(models.Model):
    product = models.ForeignKey(Product, max_length=254, blank=False, null=False, on_delete=models.CASCADE)
    in_stock = models.IntegerField(blank=True, null=True, default=0)
    issue_qty = models.IntegerField(blank=True, null=True, default=0)
    receive_qty = models.IntegerField(blank=True, null=True, default=0)

    def save(self, *args, **kwargs):
        """ Update in Stock value with order qty """
        super().save(*args, **kwargs)

    def __int__(self):
        return self.in_stock
