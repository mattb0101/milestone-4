from django.db.models.signals import post_save
from django.dispatch import receiver

from stock.models import StockTransactions


@receiver(post_save, sender=StockTransactions)
def issue_stock(sender, instance, **kwargs):
    """
    Updating stock on order
    """
    instance.product.in_stock -= instance.amount
    instance.product.save()


@receiver(post_save, sender=StockTransactions)
def receive_stock(sender, instance, **kwargs):
    """
    Updating stock on order
    """
    instance.product.in_stock += instance.amount
    instance.product.save()
