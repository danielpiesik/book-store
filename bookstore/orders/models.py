import datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Order(models.Model):

    books = models.ManyToManyField(
        'books.Book',
        related_name='orders',
    )
    buyer = models.ForeignKey(
        get_user_model(),
        related_name='orders',
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    shipping_date = models.DateField(null=True)
    order_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.shipping_date = self.calculate_shipping_date()
        super().save(*args, **kwargs)

    def calculate_shipping_date(self):
        if self.order_date.hour < datetime.time(hour=13).hour:
            return self.order_date.date()
        else:
            return (self.order_date + datetime.timedelta(days=1)).date()
