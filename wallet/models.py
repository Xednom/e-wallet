import uuid
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
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    amount_added = models.DecimalField(max_digits=8, null=True, blank=True, decimal_places=2)
    amount_deducted = models.DecimalField(max_digits=8, null=True, blank=True, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Cash'
        verbose_name_plural = 'Cashes'
        ordering = ['-date']

    def __str__(self):
        return '%s' % (self.user)
