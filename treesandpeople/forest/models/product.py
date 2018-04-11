from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import NamedBase, CostBase, TaskBase, ProductionBase


class ProductType(NamedBase):
    pass


class Product(NamedBase):
    product_type = models.ForeignKey(
        ProductType, verbose_name=_('type'),
        null=True, on_delete=models.SET_NULL
    )


class ProductBase(models.Model):
    """ Abstract base class for elements relating to Product. """

    class Meta:
        abstract = True

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)


class ProductCosts(ProductBase, CostBase):
    pass


class ProductTask(ProductBase, TaskBase):
    pass


class ProductProduction(ProductBase, ProductionBase):
    pass
