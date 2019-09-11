import uuid
from decimal import Decimal
from django.conf import settings

from django.db import models


class Cash(models.Model):
    CARD_TYPE = (
        ('Debit', 'Debit'),
        ('Credit', 'Credit')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(auto_now_add=True)
    card_details = models.CharField(max_length=150)
    card_type = models.CharField(max_length=150, choices=CARD_TYPE)
    total_amount = models.DecimalField(
        max_digits=8, decimal_places=2, default=0, null=True, blank=True)
    amount_added = models.DecimalField(
        max_digits=8, default=0, null=True, blank=True, decimal_places=2,)
    amount_deducted = models.DecimalField(
        max_digits=8, default=0, null=True, blank=True, decimal_places=2,)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Cash'
        verbose_name_plural = 'Cashes'
        ordering = ['-date']

    def __str__(self):
        return '%s' % (self.user)

    def calculate_amount(self):
        total_amount = self.total_amount + self.amount_added - self.amount_deducted
        return Decimal(total_amount)

    def save(self, *args, **kwargs):
        self.total_amount = self.calculate_amount()
        super().save(*args, **kwargs)


class Wallet(models.Model):
    CARD_TYPE = (
        ('----', '----'),
        ('Debit', 'Debit'),
        ('Credit', 'Credit')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT, unique=True)
    balance = models.DecimalField(max_digits=8, decimal_places=2,
                                  default=0, null=True, blank=True)
    card_type = models.CharField(max_length=150, choices=CARD_TYPE,
                                 default=[0][0], null=True, blank=True)
    card_number = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Balance per user'
        verbose_name_plural = 'Balance per users'
        ordering = ['-date_added']

    def __str__(self):
        return '%s - %s' % (self.user, self.balance)
