from core.models import BaseModel

from django.db import models


class Customer(BaseModel):
    login = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Customer login',
    )
    password = models.CharField(
        max_length=100,
        verbose_name='Customer password'
    )
    first_name = models.CharField(
        max_length=20,
        verbose_name='Customer first name',
    )
    surname = models.CharField(
        max_length=20,
        verbose_name='Customer surname',
    )
    email = models.EmailField(
        verbose_name='Customer email',
    )
    phone = models.PositiveIntegerField(
        max_length=12,
        verbose_name='Customer phone number',
    )
    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
