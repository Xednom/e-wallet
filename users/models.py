from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email_address = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    state = models.CharField(max_length=150, null=True, blank=True)
    zip_code = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created_at']

    def __str_(self):
        return self.username
