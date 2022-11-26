from core.models import BaseModel

from django.db import models


class Item(BaseModel):
    title = models.CharField(
        max_length=50,
        verbose_name='Item title',
    )
    description = models.TextField(
        verbose_name='Item description',
        blank=True,
        null=True
    )
    price = models.PositiveIntegerField(
        verbose_name='Item price',
    )
    published = models.DateTimeField(
        auto_now_add=True,
    )
    loc_district = models.CharField(
        max_length=50,
        verbose_name='District',
    )
    loc_city = models.CharField(
        max_length=50,
        verbose_name='City',
    )

    class Meta(BaseModel.Meta):
        pass


class Category(BaseModel):
    pass
